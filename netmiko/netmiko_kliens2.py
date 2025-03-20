from netmiko import ConnectHandler
mikrotik_device = {'device_type':'cisco_xe','host':'172.19.255.216','username':'admin','password':'cisco'}
net_connect = ConnectHandler(**mikrotik_device)
output = net_connect.send_command('wr')
print(output)
net_connect.disconnect()
