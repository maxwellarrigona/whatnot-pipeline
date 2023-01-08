import requests

url = "http://api.coincap.io/v2/assets/bitcoin"

payload = ""
response = requests.request("GET", url, data=payload)

print(response.text)
