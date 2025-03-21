from scapy.all import * 
from Hosts import IP_Host_A, IP_Host_B, BroadCast

def arp_gratuitous(src, dst, hw_dst):
    E = Ether()
    A = ARP()
    A.op = 1
    A.pdst = dst
    A.psrc = src
    A.hwdst = hw_dst
    pkt = E/A
    return pkt

pkt = arp_gratuitous(IP_Host_B, IP_Host_A, BroadCast)
pkt.show()
sendp(pkt)
