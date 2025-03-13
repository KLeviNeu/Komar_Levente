import requests, json

url= "https://"
a = ("admin", "admin")
h = {"Accept":"application/yang-data+json"} verify = False)
try:
	reply=requests.get(url, auth = a, headers = h)
except:
	print("Hiba!")
	exit()

if reply.status_code == 200:
	print(reply.json())
else:
print(reply.status_code)
print(reply.text)
