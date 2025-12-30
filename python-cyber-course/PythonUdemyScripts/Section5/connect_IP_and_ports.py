import socket

#list of ports to test
ports_test = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

#ip or honest to scan ports
target = "google.com"

print(f"Testing host connectivity: {target}")


for port in ports_test:
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.settimeout(1)  # Set a timeout for the connection attempt

#error handling for connection attempts
    try:
        client.connect((target, port))# Attempt to connect
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")
    finally:
        client.close()  # Ensure the socket is closed after the attempt

    socket.gethostbyname(target)  # Resolve hostname to IP address   
    print(f"Resolved IP address: {socket.gethostbyname(target)}") 
    