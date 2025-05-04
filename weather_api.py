import requests

def get_weather_data(api_key, location, date):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}'
    params = {
        'key': api_key,
        'unitGroup': 'metric',
        'include': 'days',
        'elements': 'datetime,temp,tempmax,tempmin,feelslike,humidity,precip,windspeed,windgust,conditions',
        'contentType': 'json'
}
    response = requests.get(url, params=params)

    # Check status and print JSON
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)