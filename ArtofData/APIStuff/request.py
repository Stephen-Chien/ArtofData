import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "d5a02e69fb194d7c93f132951201711"



locations = ["San Francisco", "Guangzhou", "-0.33237, 8.08318", "53.216.147.194"]

for i in range (0, len(locations)):

    payload = {

    "key" : key,
    'q' : locations[i]
    }

    response = requests.get(url, params = payload)

    if response.status_code == requests.codes.ok:
        data = response.json()
        print(data["current"]["wind_dir"])
    
    else:
        print(response.status_code)
        print(response.text)