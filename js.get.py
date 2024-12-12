import requests

id=input("Melyik auto erdekel? ")
car={
}

try:
	reply=requests.get("http://localhost:3000/cars/" + id)
except:
	print("Hiba!")
	exit()

if reply.status_code == 200:
	print(reply.json())

print(reply.status_code)
