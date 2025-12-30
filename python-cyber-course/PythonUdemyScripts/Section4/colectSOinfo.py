#whoami 
#ipconfig -> ip addr in linux
#tracert -> ping in linux
#netstat

#news commands:
#hostname
#tasklist -> ps aux in linux
#systeminfo -> in linux using uname -a for kernel information or hostnamectl for detailed system information.

import subprocess

user = subprocess.run(['whoami'], capture_output=True, text=True)
print("User connected:\n", user.stdout)

#network info
net = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
print("Network Information:\n", net.stdout)
#essencial for footprinting -> footprinting is the first step in ethical hacking and penetration testing, where you gather as much information as possible about a target system or network. This information helps you understand the target's structure, vulnerabilities, and potential entry points for further testing.

#complete system info
system = subprocess.run(['hostnamectl'], capture_output=True, text=True)
print("System Information: \n", system.stdout)

#kernel info
system = subprocess.run(['uname', '-a'], capture_output=True, text=True)
print("System Information: \n", system.stdout)

processes = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
print("Running Processes:\n", processes.stdout)

