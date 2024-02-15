import json
class ConfigParameters:
    def __init__(self):
        with open("./config.json") as f:
            config_data = json.load(f)
        self.api_key = config_data['AZURE_OPENAI_KEY']
        self.endpoint_url = config_data['AZURE_OPENAI_ENDPOINT']
        self.AZURE_MAPS_SUBSCRIPTION_KEY = config_data['AZURE_MAPS_SUBSCRIPTION_KEY']
        self.TOMORROWIO_API_KEY = config_data['tmrwio']
        self.bing_search_subscription_key = config_data['bing_search_subscription_key']
        self.bing_search_url = config_data['bing_search_url']
        self.deployment_name = config_data['deployment_name']
        self.azure_endpoint = config_data['azure_endpoint']
        self.api_version = config_data['api_version']
        self.aoai_api_key = config_data['aoai_api_key']