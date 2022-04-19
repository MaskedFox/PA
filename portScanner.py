#!/usr/bin/env python
import socket
import sys
from datetime import datetime

# Get host
#if len(sys.argv) == 2:
remoteServer = raw_input("Whats the hostname? ")
remoteServerIp = socket.gethostbyname(remoteServer)

print("Scanning host", remoteServer)

# time started
tStarted = datetime.now()

# Handling exceptions
try:
    for port in range(0, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pOpen = sock.connect_ex((remoteServerIp,port))
        if pOpen == 0:
	    print("Port {} is open".format(port)
        sock.close() 	

except KeyboardInterrupt:
    print("you pressed Control-C")
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved"")
    sys.exit()

except socket.error:
    print("Couldnt connect to host")
    sys.exit()

tStop = datetime.now()

totalTime = tStop - tStarted

print("Scanning completed in {}".format(totalTime)



