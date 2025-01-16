import requests

try:
	reply = requests.get("https://postman-echo.com/basic-auth",auth=("postman","password"))
except:
	print("hiba")
	exit()
print(reply.json())
print(reply.status_code)
