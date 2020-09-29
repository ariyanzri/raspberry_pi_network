import os
import time 
from datetime import date,datetime

known_mac_addresses = ["14:AB:C5:24:7D:A9","3E:B7:E1:30:FB:91","00:00:CA:01:02:03","B8:BC:5B:94:96:F1","20:F3:75:C9:67:1F"]
update_interval = 10
current_devices = []

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
		return "{0} - {1} - {2}".format(self.name,self.ip_address,self.mac_address)

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

		if ip_address == "192.168.0.2":
			continue

		dvc = Device(name,ip_address,mac_address)
		device_list.append(dvc)

	return device_list

def write_log(string):
	date_now = date.today().strftime("%d_%m_%Y")
	
	time_now = datetime.now().strftime("%H:%M:%S")
	
	if os.path.exists('/media/usb/network_logs/{0}_device_connection_log.txt'.format(date_now)):
		with open('/media/usb/network_logs/{0}_device_connection_log.txt'.format(date_now),"a+") as f:
			f.write('{0} {1} --> {2}\n'.format(date_now,time_now,string))

	else:
		with open('/media/usb/network_logs/{0}_device_connection_log.txt'.format(date_now),"w+") as f:
			f.write('{0} {1} --> {2}\n'.format(date_now,time_now,string))

while True:
	devices = get_list_devices()

	for d in devices:
		if d not in current_devices:
			write_log("Device connected: {0}".format(d))

	for d in current_devices:
		if d not in devices:
			write_log("Device disconnected: {0}".format(d))

	current_devices = devices

	time.sleep(update_interval)

