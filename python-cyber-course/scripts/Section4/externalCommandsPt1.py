import subprocess #using by os.system alternative because it's more secure and modern

command = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True)

print("Output:", command.stdout)
print("Return Code:", command.returncode)

#netstat ideal for checking network connections and listening opening ports

command = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
#-a ->open connections and listening ports, -n ->show numerical addresses instead of resolving hostnames
if command.returncode == 0:
    print("Network Connections and Listening Ports:")
    print(command.stdout)
else:
    print("Error executing netstat:", command.stderr)

#create reusinable function

def execute_command(command: list):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error executing {command}"
    
output_ping = execute_command(["ping", "-c", "1", "example.com"])
print(output_ping)

output_netstat = execute_command(["netstat", "-an"])
print(output_netstat)
