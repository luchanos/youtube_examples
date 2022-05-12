import requests

resp = requests.post("https://google.com", headers={"cookies"})
print(resp.json())
