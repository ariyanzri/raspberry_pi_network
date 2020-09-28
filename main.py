import os
import re

f = os.popen('sudo nmap -sP 192.168.0.*')
output = f.read()

connected_devices = output.split('\nNmap ')

for d in connected_devices:
# 	scan report for 192.168.0.5
# Host is up (0.048s latency).
# MAC Address: B8:BC:5B:94:96:F1 (Unknown)

	m = re.match("\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",d)
	print(m.group(0))