import socket

def validate_service(ip , port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        client.settimeout(1)
        client.connect((ip, port))
        print(f"Service on {ip}:{port} is reachable.")
        client.close()

    except:
        print(f"Service on {ip}:{port} is not reachable.")

ip_target = "scanme.nmap.org"

for port in range(20, 100):
    validate_service(ip_target, port)
