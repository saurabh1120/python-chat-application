import socket

UDP_IP = "127.0.0.1"

UDP_PORT = 5018

print("IP address",UDP_IP)

print("Port number ",UDP_PORT)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



try:

	while True:

		message=input("enter message to be sent ").encode()

		if message in [b"Q",b"q"]:

			break;

		sock.sendto(message,(UDP_IP, UDP_PORT))

	

		data, addr = sock.recvfrom(1024)

		if data in [b"Q",b"q"]:

			break;

		print(data.decode())

except Exception as e:

	print(e)	