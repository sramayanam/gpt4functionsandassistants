from openai import AzureOpenAI
class GPT4Chat:
    def __init__(self, endpoint_url, api_key):
        self.endpoint_url = endpoint_url
        self.api_key = api_key
        self.api_version = '2023-12-01-preview'
        self.client = AzureOpenAI(azure_endpoint=self.endpoint_url, api_key=self.api_key, api_version=self.api_version)

    def chat(self, message,tools=None,tool_choice = None ):

        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=message,tools=tools,tool_choice=tool_choice
        )
        return response


