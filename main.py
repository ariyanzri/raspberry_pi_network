import os
import time 

class Device:

	def __init__(self,name,ip,mac):
		self.name = name
		self.ip_address = ip
		self.mac_address = mac

	def __eq__(self,obj):
		if obj.mac_address == self.mac_address:
			return True
		return False

	def __str__(self):
		return "--- device name: ({0}) - IP address: {1} - MAC address: {2} ---".format(self.name,self.ip_address,self.mac_address)

def get_list_devices():

	device_list = []

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

		if ip_address == "" and mac_address == "" and name == "":
			continue

		if ip_address == "192.168.0.2"

		dvc = Device(name,ip_address,mac_address)
		device_list.append(dvc)

	return device_list


update_interval = 10
current_devices = []

while True:
	devices = get_list_devices()

	for d in devices:
		if d not in current_devices:
			print("Device connected: {0}".format(d))

	for d in current_devices:
		if d not in devices:
			print("Device disconnected: {0}".format(d))

	current_devices = devices

	time.sleep(20)

