import socket

UDP_IP = "127.0.0.1"

UDP_PORT = 5018



sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))



print("IP address:",UDP_IP)

print("port no.:",UDP_PORT)

print("press Q to exit ")

try:

	while True:

		data, addr = sock.recvfrom(1024)

		print(data.decode())

		if data in [b"Q",b"q"]:

			sock.sendto(b"q",(UDP_IP, addr[1]))

			break;

		message=input("enter message to be sent ").encode()

		if message in [b"Q",b"q"]:

			sock.sendto(message,(UDP_IP, addr[1]))

			break;

		sock.sendto(message,(UDP_IP, addr[1]))		

except Exception as e:

			print(e)

