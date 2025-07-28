

````markdown
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

Make sure you have a file named `code.py` in your project. It should contain the following:

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
````

---

### Step 2: Run the Scanner

1. Open a terminal or command prompt
2. Navigate to the folder containing `code.py`
3. Run the script with:

```bash
python code.py
```

4. Follow the on-screen prompts:

```
Simple Port Scanner

Enter IP: 127.0.0.1
Start port: 20
End port: 80

Scanning 127.0.0.1 from port 20 to 80...

Port 22 is open
Port 80 is open

Scan finished. Open ports: [22, 80]
```

---

## 🗂️ File Structure

```
PortScanner/
├── code.py         # Main Python script
├── README.md       # This file
```

---

## 🧪 Tested On

* ✅ Windows 10
* ✅ Ubuntu 22.04
* ✅ Python 3.9+
* ✅ Works on both localhost and LAN IPs

---

## 📚 Use Cases

* 🔍 Find open ports on your system or network
* 🧠 Learn socket programming fundamentals
* 🧪 Use in Computer Networks mini-projects
* 🛡️ Try basic security testing of LAN devices

---

## 👨‍💻 Author

Built with 💻 by **Darsh Soni and Pritisha Mishra**
For the **Computer Networks Project**

---

## 📘 License

This project is open-source and free to use for learning, academic, and personal purposes.

```
