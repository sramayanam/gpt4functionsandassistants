import tools
import json
from utils import completionscall, weather, loadtools, retrieve_links

def main():
    ## Create a tool, register the tool and add it to the fun catalog
    t = tools.tools()
    toollist = []

    for tool in t.object:
        print(tool)
        toollist.append(tool)

    ## This is a manual step to add the function to the function catalog as it is necessary to implement this in utils.py
    ## this has atmost significance since the catalog look up value should be of type function
    ## to make the generic calls
    funccatalog = {"weather": weather,"retrieve_links": retrieve_links}

    ## Create a starter message and call the loadtools function

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant who helps me dress appropriately for the weather. Please provide me a fashiaionable outfit. Please use multiple tools at your disposal"
        },
        {
            "role": "user",
            "content": "Retrieve a set of url links depending on the current weather in Frisco, Texas"
        }
    ]

    result = loadtools(tools = toollist, initprompt = messages, tool_choice = "auto")
    print(f"****** {result.model_dump_json()} #######")
    ## Append the message to the original message. 
    ## If there are tools, call the function and append the response to the messages list
    if result.choices[0].message.tool_calls:
        messages.append(result.choices[0].message)
        for tool in result.choices[0].message.tool_calls:
            if tool.function.name == "weather":
                funcname = funccatalog[tool.function.name]
                funcargs = json.loads(tool.function.arguments)
                print(funcargs)
                functoolid = tool.id
                for func in funccatalog:
                    print(f"Function Name in Catalog: {func}")
                print(f"Function Name: {funcname}, Function Args: {funcargs}, Function Tool ID: {functoolid}")
                print(type(funcargs))
                print(funcargs['location'])
                print(funcargs['unit'])
                funcresponse = funcname(location=funcargs['location'], unit=funcargs['unit'])
                messages.append(
                            {
                                "tool_call_id": functoolid,
                                "role": "tool",
                                "name": tool.function.name,
                                "content": funcresponse["content"],
                            }
                        )
                
                messages.append(
                    {
                        "role": "user",
                        "content": "Summarize the final output as a comma seperated list of fashion accessories. limit the list to 3"
                    }
                )
            elif tool.function.name == "retrieve_links":
                funcname = funccatalog[tool.function.name]
                funcargs = json.loads(tool.function.arguments)
                print(funcargs)
                functoolid = tool.id
                for func in funccatalog:
                    print(f"Function Name in Catalog: {func}")
                print(f"Function Name: {funcname}, Function Args: {funcargs}, Function Tool ID: {functoolid}")
                print(type(funcargs))
                print(funcargs['query'])
                print(funcargs['attr_filter'])
                funcresponse = funcname(query=funcargs['query'])
                messages.append(
                            {
                                "tool_call_id": functoolid,
                                "role": "tool",
                                "name": tool.function.name,
                                "content": funcresponse["content"],
                            }
                        )
            
            
            print(f"The final message is : {messages}") 
            ##make the final call
            response = completionscall(messages)
            print(response.model_dump_json())

if __name__ == "__main__":
    main()