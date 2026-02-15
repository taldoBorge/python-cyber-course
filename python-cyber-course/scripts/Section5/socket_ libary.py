#socket libary used to create network connections, like a bridge

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket objectm, AF_INET is address family for IPv4, SOCK_STREAM is for TCP

client.connect(("google.com", 80)) #Connect to google on port 80

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #Send a simple HTTP GET request, b before string indicates bytes, \r\n is carriage return and newline to format the request properly

response = client.recv(4096) #Receive up to 4096 bytes from the server

print(response.decode()) #Decode bytes to string and print the response