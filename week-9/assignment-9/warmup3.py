import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RC_KEY")

response = requests.get(
  'https://api.restcountries.com/countries/v5?region=Europe&response_fields=names.common',
  headers={'Authorization': f"Bearer {API_KEY}"}
)

response_data = response.json()

data2 = response_data["data"]["objects"]

for data in data2[:10]:
    print(data["names"]["common"])

