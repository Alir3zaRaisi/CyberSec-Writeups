# ICMP Redirect & MitM Lab – SEED Security Exercises

This project demonstrates two network-layer attacks using Scapy and Docker, based on the SEED Labs environment. The lab includes:

- **Task 1:** ICMP Redirect Attack – rerouting a victim’s traffic to a malicious router using spoofed ICMP messages.
- **Task 2:** Man-in-the-Middle (MitM) TCP packet manipulation – intercepting and modifying payloads in transit.

It also includes experimental analysis on:
- Redirecting to external or non-existent hosts
- MAC vs. IP-based packet filtering
- Sniffing direction and impact of system-level routing options

## 🧪 Lab Structure

- ICMP redirects are crafted to change the victim's routing cache.
- The MitM attack uses Scapy to sniff, modify, and re-inject TCP packets.
- Netcat is used for simulating TCP communication.
- Experiments validate attack limitations and best practices.

## 📁 Project Structure

```
ICMP-Redirect/
├── ICMP_Redirect.pdf     # Original SEED lab description
├── Writup.pdf            # Full report of the lab with code, screenshots, analysis
├── README.md             # This file
└── scripts/              # Scapy-based attack scripts
    ├── ICMP_redirect_inside.py
    ├── ICMP_redirect_outside.py
    ├── mitm_sample_ip.py
    └── mitm_sample_mac.py
```

## 🛠️ Tools Used

- Python 3 + Scapy
- Docker & Docker Compose
- Netcat
- tcpdump, mtr, ip route

## ⚠️ Disclaimer

This project is for educational and academic use only. Do **not** attempt these attacks on real or unauthorized networks.

---

Created as part of a network security lab project.
