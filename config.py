import json
class ConfigParameters:
    def __init__(self):
        with open("./config.json") as f:
            config_data = json.load(f)
        self.api_key = config_data['AZURE_OPENAI_KEY']
        self.endpoint_url = config_data['AZURE_OPENAI_ENDPOINT']
        self.AZURE_MAPS_SUBSCRIPTION_KEY = config_data['AZURE_MAPS_SUBSCRIPTION_KEY']
        self.TOMORROWIO_API_KEY = config_data['tmrwio']