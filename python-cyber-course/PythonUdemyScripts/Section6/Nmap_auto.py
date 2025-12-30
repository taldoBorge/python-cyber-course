import nmap
import datetime
from pathlib import Path

# --- DIRECTORY SETUP ---
# Define the folder where scan results will be stored
LOG_DIR = Path("logs")
# Create the directory if it doesn't exist (exist_ok prevents errors if it already exists)
LOG_DIR.mkdir(exist_ok=True)

# --- SCANNER CONFIGURATION ---
# Initialize the Nmap PortScanner object
scanner = nmap.PortScanner()

# Target host to be analyzed
target = 'scanme.nmap.org'
# Port range for the scan
ports = '20-100'

print(f"Initiating scan on {target} for ports {ports}...")

# Execute the scan with Service/Version detection (-sV)
scanner.scan(target, ports, arguments='-sV')

# --- LOGGING PREPARATION ---
# Generate a timestamp for a unique file name (YYYYMMDD_HHMMSS)
date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the full path for the log file inside the logs/ folder
archive_name = LOG_DIR / f"nmap_scan_{date_str}.log"

# --- SAVING RESULTS ---
# Open the file for writing with UTF-8 encoding
with open(archive_name, "w", encoding="utf-8") as log_file:
    # Iterate through each host discovered in the scan
    for host in scanner.all_hosts():
        # Log Host IP and its resolved hostname
        log_file.write(f"Host: {host} ({scanner[host].hostname()})\n")
        # Log the current state of the host (e.g., up)
        log_file.write(f"Stats: {scanner[host].state()}\n")
        
        # Iterate through detected protocols (TCP/UDP)
        for proto in scanner[host].all_protocols():
            # Retrieve the list of open ports for the current protocol
            open_ports = scanner[host][proto].keys()
            
            for port in open_ports:
                # Use .get() to safely access data and avoid KeyErrors
                # This ensures the script doesn't crash if a field is missing
                service = scanner[host][proto][port].get('name', 'unknown')
                product = scanner[host][proto][port].get('product', '')
                version = scanner[host][proto][port].get('version', 'N/A')
                
                # Write formatted data for each port to the log file
                log_file.write(f"Port: {port}/{proto} -> {service} | {product} {version}\n")

# Confirmation messages
print("\nScanning completed.")
print(f"Check log file: {archive_name} for detailed results.")