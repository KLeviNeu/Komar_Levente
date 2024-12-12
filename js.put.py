import requests

car={
	"id": "7",
	"brand": "Porsche",
	"model": "911",
	"production_year": 2012,
	"convertible": False
}
try:
        reply=requests.put("http://localhost:3000/cars/7", json=car)
except:
        print("Hiba!")
        exit()

print(reply.status_code)
