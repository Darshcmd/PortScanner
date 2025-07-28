# 🛡️ Python Port Scanner (Terminal-Based)

A simple and effective terminal-based port scanner using Python sockets.  
This tool helps you detect open ports on a given IP — ideal for learning basic networking and socket programming.

---

## ✨ Features

- Scans a custom port range on any IP
- Fast and responsive using timeout logic
- Pure Python — **no external libraries required**
- Simple and clean terminal interaction
- Works on localhost or any IP on your LAN

---

## 🧠 Computer Networks Concepts Applied

- **TCP/IP (Transport Layer)** — Scans using TCP sockets
- **Socket Programming** — `connect_ex()` used for probing ports
- **Client-Side Scanning** — Emulates how port scanners work
- **Timeout Handling** — Efficient scanning using short delays
- **Network Security Basics** — Understand open ports on systems

---

## 📦 Requirements

- Python 3.x
- Target IP address (e.g., `127.0.0.1`, or any LAN IP)

---

## 🚀 How to Run

### Step 1: Save the Code

Create a file named `scanner.py` and paste the following:

```python
import socket

def scan(ip, p1, p2):
    print(f"\nScanning {ip} from port {p1} to {p2}...\n")
    open_p = []

    for p in range(p1, p2 + 1):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            if s.connect_ex((ip, p)) == 0:
                print(f"Port {p} is open")
                open_p.append(p)
            s.close()
        except:
            pass

    if not open_p:
        print("No open ports found.")
    else:
        print(f"\nScan finished. Open ports: {open_p}")

# -------- Main --------
print("Simple Port Scanner")

ip = input("Enter IP: ")
p1 = int(input("Start port: "))
p2 = int(input("End port: "))

scan(ip, p1, p2)
