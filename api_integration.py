# API Integration
# This program gets the price of a cryptocurrency from the CoinGecko API.
import requests

coin = input("Enter the coin name (for example bitcoin, ethereum): ").lower()

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": coin, "vs_currencies": "usd"}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if coin in data:
        price = data[coin]["usd"]
        print("The price of", coin, "is", price, "USD")
    else:
        print("Coin not found. Please check the name.")

except requests.exceptions.RequestException:
    print("Error: the request failed. Check your internet connection.")
except ValueError:
    print("Error: the response from the API is not valid")
