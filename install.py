import platform, sys

try:
	import urllib.request as urllib_request
except ImportError:
	import urllib2 as urllib_request

def httpGet(url):
	response = urllib_request.urlopen(url)
	return response.read().decode('utf-8')

try:
	import pip
except ImportError:
	print("README: You do not have pip installed. You will have to run this script again upon completion!")
	getPip = httpGet("https://bootstrap.pypa.io/get-pip.py")
	exec(getPip)

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

pip.main(["install", wheelUrl])

print("If nothing red showed up, Pygame should be installed now.")
