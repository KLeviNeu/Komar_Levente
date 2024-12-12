import requests

car = {
	"id": "13",
	"brand": "Opel",
	"model": "Astra",
	"production_year": 2022,
	"convertible": False
}

try:
        reply=requests.post("http://localhost:3000/cars/", json=car)
except:
        print("Hiba!")
        exit()

print(reply.status_code)
