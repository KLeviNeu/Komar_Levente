import requests, json

url= "https://172.19.255.216/restconf/data/ietf-system:system/authentication/user=Admin"
a = ("admin", "admin")
h = {"Accept":"application/yang-data+json"}
try:
	reply=requests.get(url, auth = a, headers = h, verify = False)
except:
	print("Hiba!")
	exit()

if reply.status_code == 200:
	print(reply.json())
else:
	print(reply.text)
print(reply.status_code)
