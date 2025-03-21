from scapy.all import * 
from Hosts import IP_Host_A, IP_Host_B


def arp_request(src, dst):
    E = Ether()
    A = ARP()
    A.op = 1
    A.pdst = dst
    A.psrc = src
    pkt = E/A
    return pkt


pkt = arp_request(IP_Host_B, IP_Host_A)
pkt.show()
sendp(pkt)
