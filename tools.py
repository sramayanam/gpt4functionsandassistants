class tools:
    def __init__(self):
        self.object = [{
                "type": "function",
                "function": {
                    "name": "weather",
                    "description": "Get the weather for a city in celsius",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA"
                            },
                            "unit": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"]
                            }
                        },
                        "required": ["location"]
                    }
                }},
        {   
                "type": "function",
                 "function": {                   
                    "name": "retrieve_links",
                    "description": "Search and Retrieve links of apparel websites from the Azure AI Search index",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The query string to search the appropriate attire",
                            }
                        },
                        "required": ["query"]
                    }
                }
           } ]
       
