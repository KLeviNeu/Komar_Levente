#!/usr/bin/env python3
from ncclient import manager

# Device connection details
host = "172.19.255.216"
username = "admin"
password = "cisco"
interface = "GigabitEthernet0/2"
new_ip = "192.168.1.1"
new_mask = "255.255.255.0"

# Configuration payload
config = f"""
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>{interface.split('/')[-1]}</name>
        <ip>
          <address>
            <primary>
              <address>{new_ip}</address>
              <mask>{new_mask}</mask>
            </primary>
          </address>
        </ip>
      </GigabitEthernet>
    </interface>
  </native>
</config>
"""

try:
    # Connect to the device via NETCONF
    with manager.connect(
        host=host,
        port=830,
        username=username,
        password=password,
        hostkey_verify=False,
    ) as m:
        # Send the configuration change
        response = m.edit_config(target="running", config=config)
        print("Configuration applied successfully:")
        print(response)
except Exception as e:
    print(f"An error occurred: {e}")

