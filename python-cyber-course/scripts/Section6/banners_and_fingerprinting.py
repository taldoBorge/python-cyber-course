#banner and fingerprinting.
#banner is the text that a server sends to identify itself when a client connects.
#fingerprinting is the process of collecting information about a server's software and configuration based on its banner and other characteristics.
import socket

def banner_grabber(ip, port):
    try:
        # Create a socket connection to the target IP and port
        s = socket.socket()
        s.settimeout(2)
        #conect ip and port
        s.connect((ip, port))
        
        # Receive the banner
        banner = s.recv(1024)

        print(f"[+] Banner from {ip}:{port} -> {banner.decode().strip()}")

    except Exception as e:
        print(f"[-] Could not connect to {ip}:{port} -> {e}")
    finally:
        s.close()

#usage example
target_ip = "scanme.nmap.org"
target_ports = [21, 22, 25, 80, 110, 443]

for port in target_ports:
    banner_grabber(target_ip, port)