import os
import requests

API_KEY = os.getenv("KEY")

url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&country=us&prioritydomain=top"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
elif response.status_code == 429:
    print("Rate limit reached. Try again later.")
else:
    print("Request failed", response.status_code)