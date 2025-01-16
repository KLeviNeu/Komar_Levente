import requests
url = "https://api.thecatapi.com/v1/breeds"
h = {"x-api-key":"DEMO-API-KEY"}
try:
	reply=requests.get(url, headers = h)
except:
	print("Hiba!")
	exit()

if reply.status_code == 200:
	print(reply.json())
else
	print(reply.status_code)
