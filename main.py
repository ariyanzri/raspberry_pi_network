import os

f = os.popen('sudo nmap -sP 192.168.0.*')
output = f.read()

lines = output.split('\n')

for l in lines:
	print(l)