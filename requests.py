import requests

url = "https://www.google.com"
res = requests.get(url)
print("Status:", res.status_code)
