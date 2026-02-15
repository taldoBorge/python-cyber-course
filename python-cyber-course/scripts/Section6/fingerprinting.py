#fingerprinting example
import socket

target_ip = "scanme.nmap.org"
target_port = 80

#TCP conection to grab banners
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target_ip, target_port))

sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
response = sock.recv(1024).decode(errors='ignore')

print("---Baner Grabbing---")
print(response)

sock.close()