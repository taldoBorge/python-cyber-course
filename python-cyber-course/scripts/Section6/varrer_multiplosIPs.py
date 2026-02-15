import socket
import threading
from queue import Queue
from datetime import datetime
import csv

# =========================
# Terminal color definitions
# =========================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# =========================
# Global lock for thread-safe writes
# =========================
results_lock = threading.Lock()

# ==========================================================
# Function: grab_banner
# Purpose : Attempts to read initial data sent by the service
# Notes   : Some protocols (HTTP, HTTPS) do NOT send data
# ==========================================================
def grab_banner(sock):
    try:
        sock.settimeout(2)
        data = sock.recv(1024).decode(errors="ignore")

        # SSH sends more than just a banner; keep only first line
        if data:
            return data.splitlines()[0].strip()

        return "no banner"

    except socket.timeout:
        return "timeout"
    except:
        return "error"

# ==========================================================
# Function: identify_service
# Purpose : Very simple service fingerprinting by banner content
# Warning : This is heuristic, NOT guaranteed detection
# ==========================================================
def identify_service(port, banner):
    banner = banner.lower()

    if port == 22 and "ssh" in banner:
        return "SSH"
    if port in (80, 8080) and "http" in banner:
        return "HTTP"
    if port == 21 and "ftp" in banner:
        return "FTP"
    if port == 25:
        return "SMTP"
    if port == 110:
        return "POP3"
    if port == 143:
        return "IMAP"
    if port == 3306:
        return "MySQL"
    if port == 27017:
        return "MongoDB"

    return "Unknown"

# ==========================================================
# Function: scan_port
# Purpose : Attempts TCP connection to a single port
# Thread  : Safe (uses lock when writing results)
# ==========================================================
def scan_port(target, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((target, port))

        banner = grab_banner(sock)
        service = identify_service(port, banner)

        with results_lock:
            results.append((port, "open", service, banner))

        print(f"{GREEN}[OPEN]{RESET} Port {port:5} | Service: {service}")

    except socket.timeout:
        with results_lock:
            results.append((port, "filtered", "", "timeout"))
        print(f"{YELLOW}[FILTERED]{RESET} Port {port:5}")

    except ConnectionRefusedError:
        with results_lock:
            results.append((port, "closed", "", "refused"))
        print(f"{RED}[CLOSED]{RESET} Port {port:5}")

    except:
        with results_lock:
            results.append((port, "error", "", "unknown error"))
        print(f"{RED}[ERROR]{RESET} Port {port:5}")

    finally:
        sock.close()

# ==========================================================
# Function: threaded_scan
# Purpose : Multi-threaded port scanning engine
# ==========================================================
def threaded_scan(target, ports, max_threads=20):
    results = []
    queue = Queue()

    for port in ports:
        queue.put(port)

    def worker():
        while not queue.empty():
            port = queue.get()
            scan_port(target, port, results)
            queue.task_done()

    threads = []
    for _ in range(min(max_threads, len(ports))):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        threads.append(t)

    queue.join()
    return results

# ==========================================================
# Function: save_report
# Purpose : Save results to TXT and CSV files
# ==========================================================
def save_report(target, results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_name = f"scan_{target}_{timestamp}.txt"
    csv_name = f"scan_{target}_{timestamp}.csv"

    with open(txt_name, "w", encoding="utf-8") as txt:
        txt.write(f"Scan report for {target}\n")
        txt.write(f"Date: {datetime.now()}\n\n")

        for port, state, service, banner in results:
            txt.write(
                f"Port {port:5} | State: {state:8} | "
                f"Service: {service:10} | Banner: {banner}\n"
            )

    with open(csv_name, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Port", "State", "Service", "Banner"])
        for row in results:
            writer.writerow(row)

    print(f"\n{YELLOW}Reports saved: {txt_name}, {csv_name}{RESET}")

# ==========================================================
# Main execution flow
# ==========================================================
def main():
    print(f"{YELLOW}=== Advanced Port Scanner (Educational) ==={RESET}")

    target = input("Target IP or hostname: ").strip()

    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 143,
        443, 3306, 3389, 8080, 27017
    ]

    results = threaded_scan(target, common_ports)
    save_report(target, results)

    print(f"\n{GREEN}Scan completed.{RESET}")

if __name__ == "__main__":
    main()
