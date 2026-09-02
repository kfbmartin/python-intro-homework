import requests

url = "https://thisurldoesnotexist.example.com"
try:
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Request failed: status {response.status_code}")
        
    else:
        data = response.json()
        # work with data here
except requests.exceptions.RequestException as e:
    print(f"Error: Could not reach the server. Check your connection and try again.")