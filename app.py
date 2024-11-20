import os

import requests
from dotenv import load_dotenv

load_dotenv()

query = "What is histogram in statistics?"
API_KEY = os.getenv('API_KEY')

url = "https://payload.vextapp.com/hook/O5H10BJ098/catch/hello"

payload = {
    "payload": "What is histogram in statistics?"
}

headers = {
    "content-type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)