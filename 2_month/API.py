import requests

api_key = "iwQ1PwXAQ9H2NjwyQx0d4YuGURQD2b3o"
url = "https://api.giphy.com/v1/gifs/search"


user_input = input("Search for GIF: ")


params = {
    'api_key': api_key,
    'q': user_input,
    'limit': 5
}

response = requests.get(url, params)

if response.status_code == 200:
    data = response.json()
    for gif in data['data']:
        print(gif['url'])
else:
    print("Error:", response.status_code)