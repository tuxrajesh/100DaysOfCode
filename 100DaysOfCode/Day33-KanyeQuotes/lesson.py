import requests
API_URL = "https://api.sunrise-sunset.org/json"
API_PARAMETERS = {
    "lat":37.70,
    "lng":-121.9,
    "tzid":"America/Los_Angeles"
}
response = requests.get(API_URL, params=API_PARAMETERS)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)