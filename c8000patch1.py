import requests, json

url= "https://172.19.255.216:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
a = ("admin", "admin")
h = {"Accept":"application/yang-data+json"}
d = """
<interface xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <name>GigabitEthernet2</name>
    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
    <enabled>true</enabled>
    <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
            <ip>192.168.1.1</ip>
            <netmask>255.255.255.0</netmask>
        </address>
    </ipv4>
</interface>
"""
try:
	reply=requests.patch(url, auth = a, headers = h, verify = False, data = d)
except:
	print("Hiba!")
	exit()

if reply.status_code == 200:
	print(reply.json())
else:
	print(reply.text)
print(reply.status_code)
