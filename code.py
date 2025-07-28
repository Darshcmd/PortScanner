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
