# ICMP Redirect & MitM Lab – SEED Security Exercises

This project demonstrates two powerful network-level attacks using ICMP redirect and packet manipulation techniques in a Dockerized lab environment, inspired by the SEED Labs framework.

It includes:

- **Task 1:** ICMP Redirect Attack to reroute a victim's traffic through a malicious router.
- **Task 2:** Man-in-the-Middle (MitM) TCP payload manipulation attack using Scapy.
- **Analysis Section:** Answers to experimental questions about edge cases, packet direction, and filter strategy.

## 🛠️ Techniques Covered

- ICMP Redirect (Type 5, Code 0) spoofing with Scapy
- Network-wide redirection using forged gateway suggestions
- TCP sniff-and-spoof with payload rewriting
- MAC-based vs IP-based packet filtering
- Manipulating the Linux routing cache
- Disabling IP forwarding and using custom forwarding logic

## 💾 Files Included

- `ICMP_Redirect.pdf`: Full lab report with code, screenshots, and experiment analysis
- `scripts/`
  - `ICMP_redirect_inside.py`
  - `ICMP_redirect_outside.py`
  - `mitm_sample_mac.py`
  - `mitm_sample_ip.py`
- `README.md`: This file

## 🔍 Tools Used

- Docker Compose
- Scapy (Python 3)
- Netcat
- tcpdump, mtr, ip route

## ⚠️ Disclaimer

This project is for educational and academic use only. Do **not** attempt these attacks on real or unauthorized networks.

---

Created as part of a network security lab project.
