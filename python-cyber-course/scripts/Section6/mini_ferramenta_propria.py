import socket

def collect_banner(sock):
    try:
        sock.settimeout(2)
        return sock.recv(1024).decode(errors='ignore')
    except:
        return None

def scan(ip, ports):
    result = []
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((ip, port))
            
            banner = collect_banner(sock)
            result.append((port, banner if banner else "No banner"))
            
            sock.close()
        except:
            # porta fechada → apenas ignora
            continue
    return result

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
    
    scan_results = scan(target_ip, ports_to_scan)

    with open("results.txt", "w", encoding="utf-8") as result_file:
        for port, banner in scan_results:
            line = f"Port: {port}, Banner: {banner}\n"
            result_file.write(line)
            print(line.strip())

    print("Scan complete. Results saved to results.txt.")
