import requests

response = requests.get(
  'https://api.restcountries.com/countries/v5?region=Europe&response_fields=names.common&limit=10',
  headers={'Authorization': 'Bearer rc_live_263a59a4f1a040cbafdfa9c16f183edc'}
)

response_data = response.json()

data2 = response_data["data"]["objects"]

for data in data2:
    print(data["names"]["common"])

