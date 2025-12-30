import nmap
#simple scanner
scanner = nmap.PortScanner()
scanner.scan('192.168.15.1', '22-80')

#listing all hosts
print(scanner.all_hosts())
#host up or down
print(scanner['192.168.15.1'].state())
#all scanned protocols
print(scanner['192.168.15.1'].all_protocols())
#list all ports for a protocol
print(scanner['192.168.15.1'].keys())

#technical report
for host in scanner.all_hosts():
    print(f"\nHost: {host}")
    print(f"State: {scanner[host].state()}")

for proto in scanner[host].all_protocols():
    print(f"Protocol: {proto}")

#obtaining all scanned ports, dictionary
ports = scanner[host][proto].keys()

#iterating over ports
for port in sorted(ports):
    state = scanner[host][proto][port]['state']
    print(f"Port: {port}\tState: {state}")

