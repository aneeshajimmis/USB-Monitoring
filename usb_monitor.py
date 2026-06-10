import pyudev
import json
import logging
import hashlib

from datetime import datetime

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


#load allowlist
with open("allowlist.json") as f:
        allowlist = json.load(f)

#configure logging
logging.basicConfig(
	filename='usb_audit.log',
	level=logging.INFO,
	format="%(asctime)s - %(message)s"
	)

#hashing
def calculate_hash(filepath):
	sha256=hashlib.sha256()
	try:
		with open(filepath,"rb") as file:
			while True:
				chunk=file.read(4096)
				if not chunk:
					break
				sha256.update(chunk)
		return sha256.hexdigest()
	except Exception as e:
		return f"HASH ERROR: {e}"

#watchdog
class  USBWatcher(FileSystemEventHandler):
	def on_created(self, event):
		global files_created
		if event.src_path.startswith("./test_usb/."):
			return
		if not event.is_directory:
			files_created +=1
			print("\nFile created:")
			print(event.src_path)
			file_hash=calculate_hash(event.src_path)
			print("SHA256:")
			print(file_hash)
			logging.info(
				"File Created | "
				+ event.src_path
				+" | SHA256="
				+ file_hash
			)
	def on_modified(self, event):
		global files_modified
		if event.src_path.startswith("./test_usb/."):
			return
		if not event.is_directory:
			files_modified +=1
			print("\nFile modified:")
			print(event.src_path)
			file_hash=calculate_hash(event.src_path)
			print("SHA256:")
			print(file_hash)
			logging.info(
				"File Modified | "
				+ event.src_path
				+" | SHA256="
				+ file_hash
			)

	def on_deleted(self, event):
		global files_deleted
		if event.src_path.startswith("./test_usb/."):
			return
		if not event.is_directory:
			files_deleted +=1
			print("\nFile deleted:")
			print(event.src_path)
			logging.info(
				"File deleted | "+ event.src_path
			)

#create USB monitor
context = pyudev.Context();

monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

print("=" * 50)
print("USB device control & Monitoring Framework")
print("monitoring USB devices... ")
print("=" * 50)

#statistics counters
total_devices=0
authorized_devices=0
blocked_devices=0


files_created=0
files_modified=0
files_deleted=0


observer =Observer()
observer.schedule(
	USBWatcher(),
	"./test_usb",
	recursive=True
)

observer.start()

try:
	for action, device in monitor:
		print(f"\nAction: {action}")

		vendor= device.get('ID_VENDOR_ID')
	
	
		product= device.get('ID_MODEL_ID')
	

		serial= device.get('ID_SERIAL_SHORT')
	


		if vendor is None:
			continue

		authorized=False

		for dev in allowlist["devices"]:
			if(
				vendor == dev["vendor"]
				and product ==dev["product"]
				and serial==dev["serial"]
			):
				authorized=True

		print("\n-----------------")

		print("Action :",action)
		print("vendor :",vendor)
		print("product :",product)
		print("serial :",serial)
	
		if authorized:
			total_devices+=1
			authorized_devices+=1
		
			print("Authorized devices")
			logging.info(
				f"AUTHORIZED | Action={action} | Vendor={vendor} | Product={product} | Serial={serial}"
			)
		else:
			total_devices+=1
			blocked_devices+=1

			print("unauthorized devices")
			print("Blocked Devices")
			logging.info(
                        	f"UNAUTHORIZED | Action={action} |  Vendor={vendor} | Product={product} | Serial={serial}"
                	)


except KeyboardInterrupt:

	print("\n\nGenerating Secuirty Report..")
	report=f"""
	USB SECUIRTY REPORT
	==================
	Generated ON:
	{datetime.now()}

	Total devices seen :{total_devices}
	Authorized devices :{authorized_devices}
	Blocked devices :{blocked_devices}

	File Activity
	-------------

	Files Created : {files_created}
	Files Modified :{files_modified}
	Files Delected :{files_deleted}

	Log Files:
	usb_audit.log
	"""

	with open("report.txt","w") as f:
		f.write(report)
	print(report)
	print("Report saved as report.txt")

