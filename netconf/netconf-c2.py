from ncclient import manager

DEVICE = {
    "host": "172.19.255.216",  # Replace with your device's IP
    "port": 830,
    "username": "admin",
    "password": "cisco",
    "hostkey_verify": False
}

INTERFACE_CONFIG = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>0/2</name>
        <ip>
          <address>
            <primary>
              <address>192.168.2.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </GigabitEthernet>
    </interface>
  </native>
</config>"""

def main():
    with manager.connect(**DEVICE) as m:
        print("Connected to the device.")
        response = m.edit_config(target="running", config=INTERFACE_CONFIG)
        print("Response from the device:")
        print(response)

if __name__ == "__main__":
    main()

