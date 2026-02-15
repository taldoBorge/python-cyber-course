import subprocess

def execute_command(command: list):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error executing {command}"

#saving ping output to a log file for auditing posteriorly
with open("log_netstat.txt", "w") as log: #This function and logic are used in practice for auditing purposes.
    log.write(execute_command(["netstat", "-an"]))

              
