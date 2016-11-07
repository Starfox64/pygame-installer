import platform, sys, os, ensurepip

ensurepip.bootstrap()

try:
	import pip
except ImportError:
	print("Error: Failed to install pip, make sure you are running this script as admin.")
	sys.exit()

arch = platform.architecture()[0]
wheelUrl = "https://raw.githubusercontent.com/Starfox64/pygame-installer/master/wheels/"

print("You are using Python" + str(sys.version_info[0]) + str(sys.version_info[1]) + " " + arch + ".")

if sys.version_info[0] == 2 and sys.version_info[1] == 7:
	if arch == "64bit":
		wheelUrl += "pygame-1.9.2b1-cp27-cp27m-win_amd64.whl"
	else:
		wheelUrl += "pygame-1.9.2b1-cp27-cp27m-win32.whl"
elif sys.version_info[0] == 3 and sys.version_info[1] in (4, 5, 6):
	if sys.version_info[1] == 4:
		if arch == "64bit":
			wheelUrl += "pygame-1.9.2b1-cp34-cp34m-win_amd64.whl"
		else:
			wheelUrl += "pygame-1.9.2b1-cp34-cp34m-win32.whl"
	elif sys.version_info[1] == 5:
		if arch == "64bit":
			wheelUrl += "pygame-1.9.2b1-cp35-cp35m-win_amd64.whl"
		else:
			wheelUrl += "pygame-1.9.2b1-cp35-cp35m-win32.whl"
	elif sys.version_info[1] == 6:
		if arch == "64bit":
			wheelUrl += "pygame-1.9.2b8-cp36-cp36m-win_amd64.whl"
		else:
			wheelUrl += "pygame-1.9.2b8-cp36-cp36m-win32.whl"
else:
	print("Pygame only supports Python 27, 34, 35 and 36.")
	sys.exit()

if pip.main(["install", wheelUrl]) == 0:
	print("Pygame should now be installed.")
else:
	print("Something went wrong during the installation of pygame.")

os.system("pause")
