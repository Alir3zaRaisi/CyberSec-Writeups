# Reverse Engineering Writeups – Stack Overflow Basics

This repository contains a detailed reverse engineering and binary exploitation challenge focused on basic stack-based buffer overflows.

## 🔹 Challenge: `exercise1`

This is a classic CTF-style binary that contains:

- A vulnerable `gets()` call
- A local integer (`local_c`) used in a conditional branch
- A `helloUser()` function with another buffer overflow opportunity
- A hidden `secret()` function that we want to reach

### Exploit Goals

- Overwrite local variables to manipulate control flow
- Hijack the return address to jump to `secret()`

### Files Included

```
.
├── exercise1              # Binary file (compiled ELF)
├── exercise1.gzf          # Ghidra project file (for analysis)
├── Overflow-basic-1.pdf   # PDF version of the LaTeX writeup
├── Payload1.py            # Two-stage exploit (overflow + ret overwrite)
├── Payload2.py            # Direct return-to-secret exploit
```

### ✅ Quick Run

Make sure `pwntools` is installed:

```bash
pip install pwntools
```

Then run either exploit:

```bash
python3 Payload1.py
# or
python3 Payload2.py
```

### 🧠 Writeup

The full explanation of the vulnerability, Ghidra-based offset analysis, payload construction, and exploitation steps can be found in:

- `Overflow-basic-1.pdf`: Full technical explanation with offset breakdown
- `exercise1.gzf`: Load into Ghidra to view function layout and variable offsets

---

## 🛠 Tools Used

- 🔍 Ghidra — static analysis and offset discovery
- 💣 Pwntools — exploit development
- 🧠 Manual reasoning based on stack layout

---

## 📎 License

Educational use only. Please do not redistribute binaries without permission.
