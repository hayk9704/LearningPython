import requests
link = requests.get("https://api.coincap.io/v2/assets/bitcoin")
print(link.json())