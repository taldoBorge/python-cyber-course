#http codes
#200 OK
#401 Unauthorized
#403 Access Forbidden
#404 Not Found
#500 Internal Server Error

from collections import Counter

#create a log file

log_archive = 'logs/log.log'

#list to store the suspected events
suspected_events = []

#read the log file
with open(log_archive, 'r', encoding='utf-8') as log_file:
    for line in log_file:
        parts = line.strip().split(' - ')
        if len(parts) != 4:
            continue  # Skip malformed lines
        timestamp, ip_address, request, status_code = parts
        status_code = int(status_code)
        #suspect status codes
        if status_code in [401]:
            suspected_events.append(ip_address)

#count suspect IPs
suspects_count = Counter(suspected_events)

print("Suspected IP addresses and their counts:")
for ip, count in suspects_count.items():
    print(f"IP Address: {ip}, Count: {count}")

#save the suspected events to a file
with open('logs/suspected_events.txt', 'w', encoding='utf-8') as output_file:
    for ip, count in suspects_count.items():
        output_file.write(f"IP Address: {ip}, Count: {count}\n")