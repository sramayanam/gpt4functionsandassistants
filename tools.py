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
                    "name": "retrieve_images",
                    "description": "Search and Retrieve images of clothes from the Azure AI Search index",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The query string to search for attire",
                            },
                            "attr_filter": {
                                "type": "string",
                                "description": "The odata filter to apply for the fashion attributes field. Only actual ingredient names should be used in this filter. If you're not sure something is a fashion item, don't include this filter. Example: fashionelements/any(i: i eq 'shoe' or i eq 'pants')",
                            }
                        },
                        "required": ["query"]
                    }
                }
           } ]
       
