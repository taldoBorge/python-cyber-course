'''
#snifing -> capturing packets from the network, #spoofing -> creating fake packets or modifying existing ones

from scapy.all import sniff

#function to process each captured packet
def reciver_packet(packet):
    print(packet.summary()) #print a summary of the packet

#start sniffing packets in interface 'eth0'
sniff(count = 20, prn=reciver_packet) 
'''

#spoofing example
from scapy.all import IP, ICMP, send

# Create packet IP with destination and origin
packet = IP(src="10.0.0.123", dst="8.8.8.8")

print("Sending packet ICMP with fake origin IP")
send(packet)