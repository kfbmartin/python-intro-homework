import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RC_KEY2")

#API key as a header
url = "https://api.restcountries.com/countries/v5"

headers = {'Authorization': API_KEY}

def fetch_countries(params):
    #API request
    try: 
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
                print(f"Request failed: status {response.status_code}")
                return []

        else: 
            data = response.json()
            countries_list = data['data']['objects']

    except requests.exceptions.RequestException:
        print("Error: Could not reach the server. Check your connection and try again.")
        return[]
    
    # Clean API results
    cleaned = []

    for country in countries_list:
        cleaned.append({
            "name": country["names"]["common"],
            "capitals": country["capitals"][0]["name"] if country.get("capitals") else "N/A",
            "region": country["region"],
            "population": country["population"]
        })

    return cleaned
  
def show_menu():
    #Print Country Explorer Menu
    print("")
    print("=== Country Explorer ===")
    print("1. Search by name")
    print("2. Filter by region")
    print("3. Quit")
    print("")

    option = input("Choose an option (1-3):")
    return option

#Quit Loop

def quit_loop():
    print("Quit Country Explorer")
    
def main():
    while True: 
        result = show_menu()
        if result == "1":
            search_term = input("Please enter a search term: ")

            params = {
                "response_fields": "names.common, capitals, region, population",
                "limit":100,
                  "names.common":search_term
            }

            countries = fetch_countries(params)

            sorted_cleaned_countries = sorted(countries, key=lambda country: country["population"],reverse=True)

            for country in sorted_cleaned_countries:
                print(f"{country['name']} | Capital: {country['capitals']} | Region: {country['region']} | Population: {country['population']} ")
            
        elif result == "2":
            region_name = input("Please enter the region name: ")

            params = {
                "response_fields": "names.common, capitals.name, region, population",
                "limit":100,
                "region":region_name
            }
            countries = fetch_countries(params)

            sorted_cleaned_countries = sorted(countries, key=lambda country: country["population"],reverse=True)
            
            for country in sorted_cleaned_countries:
                print(f"{country['name']} | Capital: {country['capitals']} | Region: {country['region']} | Population: {country['population']} ")              

        elif result == "3":
            quit_loop()
            break

        else:
            print("Please enter a number between 1 and 3.")

main()