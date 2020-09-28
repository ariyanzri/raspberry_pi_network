import os

f = os.popen('sudo nmap -sP 192.168.0.*')
output = f.read()

connected_devices = output.split('\nNmap ')

for d in connected_devices:

	ip_address = ""
	mac_address = ""
	name = ""

	lines = d.split('\n')

	for l in lines:
		if "scan report for" in l:
			ip_address = l.split("for ")[1]

		elif "MAC Address" in l:
			temp = l.split("Address: ")[1]
			mac_address = temp.split(" ")[0]
			name = temp.split(" ")[1].replace('(','').replace(')','')

	print("Device Name: ({0}) - Device IP: ({1}) - Device MAC: ({2})".format(name,ip_address,mac_address))