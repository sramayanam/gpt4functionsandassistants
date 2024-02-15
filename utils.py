import config
import core
import requests
import json

config_params = config.ConfigParameters()

def retrieve_images(query, attrfilter):
    pass

def loadtools(tools,initprompt,tool_choice = "auto"):
    endpoint_url = config_params.endpoint_url
    api_key = config_params.api_key
    gpt4_chat = core.GPT4Chat(endpoint_url, api_key)
    response = gpt4_chat.chat(message = initprompt,tools=tools,tool_choice=tool_choice)
    return response

def getLatLong(address):
    params = {
        'subscription-key': config_params.AZURE_MAPS_SUBSCRIPTION_KEY,
        'api-version': '1.0',
        'language': 'en-US',
        'query': address
    }

    response = requests.get('https://atlas.microsoft.com/search/address/json', params=params)
    data = response.json()

    try:
        lat = data['results'][0]['position']['lat']
        lon = data['results'][0]['position']['lon']
    except (IndexError, KeyError) as e:
        print(f'Error: {e}')
        return None

    return lat, lon

def weather (location,unit):
    lat, lon = getLatLong(location)
    print(f"Lat: {lat}, Lon: {lon}")
    url = "https://api.tomorrow.io/v4/weather/forecast?location=" + str(lat) + "," + str(lon) + "&apikey=" + config_params.TOMORROWIO_API_KEY
    payload = {}
    headers = {
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    print(resp['timelines']["hourly"][0]["values"]["temperature"])
    return {"content": "The weather in " + location + " " + str(resp['timelines']["hourly"][0]["values"]["temperature"]) + " " +  unit }

def completionscall(fprompt):
    config_params = config.ConfigParameters()
    endpoint_url = config_params.endpoint_url
    api_key = config_params.api_key
    gpt4_chat = core.GPT4Chat(endpoint_url, api_key)
    response = gpt4_chat.chat(message = fprompt)
    return response