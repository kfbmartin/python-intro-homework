import requests

response = requests.get("https://api.agify.io/?name=michael")
response_json = response.json()

birthday_key = response_json.get("birthday")
birthday = birthday_key[0] if birthday_key else "Not available"


print(f"Name: {response_json["name"]}")
print(f"Predicted age: {response_json["age"]} ")
print(f"Birthday: {birthday}")


