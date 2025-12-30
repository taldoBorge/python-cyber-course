import os # The OS library allows direct integration with the operating system, acting as a bridge to simpler, more superficial things.

print("Current directory:", os.getcwd()) #print the current working directory

archives = os.listdir('.')
print("Files and directories in: ", os.getcwd(), " : ", archives) #list all files and directories in the current directory

import subprocess #It serves the same purpose as the OS, but we use it when we need more control over an action.

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("Listing files using subprocess:\n", result.stdout)

#verify stats

command = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True) #ping google.com
if command.returncode == 0:
    print("Ping successful")
else:
    print("Ping failed, no internet connection")
