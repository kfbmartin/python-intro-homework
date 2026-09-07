import requests

url = "https://thisurldoesnotexist.example.com"
try:
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Request failed with status code {response.status_code}")
        
    else:
        data = response.json()

        # work with data here
except requests.exceptions.RequestException:
    print("Error: Could not reach the server. Check your connection and try again.")