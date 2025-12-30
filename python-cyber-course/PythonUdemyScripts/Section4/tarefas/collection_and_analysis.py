import subprocess

net = subprocess.run(["ip", "addr"], capture_output=True, text=True)
with open("log_net.txt", "w") as log:
    log.write(net.stdout)

kernel = subprocess.run(["uname", "-r"], capture_output=True, text=True)
with open("log_kernel.txt", "w") as log:
    log.write(kernel.stdout)    

system = subprocess.run(['hostnamectl'], capture_output=True, text=True)
with open("log_system.txt", "w") as log:
    log.write(system.stdout)

print("Network and system information saved to log files.")
print("Analyzing saved network information --- IGNORE ---")
with open("log_net.txt", "r") as log:
    content = log.read()
    print("Log content:", content)

print("Analyzing saved kernel information --- IGNORE ---")
with open("log_kernel.txt", "r") as log:
    content = log.read()
    print("Log content:", content)

print("Analyzing saved system information --- IGNORE ---")
with open("log_system.txt", "r") as log:
    content = log.read()
    print("Log content:", content)