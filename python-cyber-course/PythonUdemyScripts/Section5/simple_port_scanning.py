#21 = ftp, #22 = ssh, #23 = telnet, #25 = smtp, #53 = dns, #80 = http, #110 = pop3, #143 = imap, #443 = https, #3306 = mysql

import socket

#ip or domain to scan ports
target = "192.168.15.1"

#range of ports to scan
start_port = 1
end_port = 100

for port in range(start_port, end_port + 1):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#IPv6 and TCP
    client.settimeout(1)  # Set a timeout for the connection attempt

    conection = client.connect_ex((target, port))

    if conection == 0:
        print(f"Port {port} is open")

    else:
        print(f"Port {port} is closed")

    client.close()  # Ensure the socket is closed after the attempt

    