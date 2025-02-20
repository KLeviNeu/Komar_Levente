from netmiko import ConnectHandler
mikrotik_device = {'device_type':'mikrotik_routeros','host':'172.17.255.195','username':'admin','password':'admin'}
net_connect = ConnectHandler(**mikrotik_device)
output = net_connect.send_command('/ip address print')
print(output)
net_connect.disconnect()
