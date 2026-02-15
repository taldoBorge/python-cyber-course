import subprocess

#saving network information to a file
command = subprocess.run(["ip", "addr"], capture_output=True, text=True)
with open("log_net.txt", "w") as log:
    log.write(command.stdout)

print("Network information saved to log_net.txt")

#analyzing saved information

with open("log_net.txt", "r") as log:
    content = log.read()

print("Log content:", content)