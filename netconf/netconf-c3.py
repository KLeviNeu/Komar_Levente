from ncclient import manager
from lxml import etree

# Device connection details
DEVICE = {
    "host": "172.19.255.216",  # Replace with your device's IP address
    "port": 830,
    "username": "admin",
    "password": "cisco",
    "hostkey_verify": False
}

# Define a function to save XML to a file
def save_to_file(filename, xml_data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(xml_data)

def main():
    with manager.connect(**DEVICE) as m:
        print("Connected to the device.")
        
        # Retrieve configuration using NETCONF
        response = m.get_config("running")

        # Remove encoding declaration if present
        xml_without_declaration = response.xml.replace('<?xml version="1.0" encoding="UTF-8"?>', "").strip()

        # Convert the response to pretty-printed XML
        xml_pretty = etree.tostring(
            etree.fromstring(xml_without_declaration), pretty_print=True
        ).decode()

        # Save the output to a file
        output_file = "output.xml"
        save_to_file(output_file, xml_pretty)
        
        print(f"Configuration saved to {output_file}")

if __name__ == "__main__":
    main()

