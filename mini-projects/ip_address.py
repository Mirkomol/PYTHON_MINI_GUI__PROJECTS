import socket

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

print("My Ip address: " + ipAddress)