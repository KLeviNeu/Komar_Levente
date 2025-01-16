import requests
try:
	reply = requests.get(input("URL: "), timeout = 5)
	print(reply.text)
	print(reply.status_code)
except requests.exceptions.Timeout:
	print("Kerem legyen turelmesebb")
except:
	print("hiba")
