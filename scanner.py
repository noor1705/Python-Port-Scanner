
import socket

print("--------------------------------")
print("       PYTHON PORT SCANNER")
print("--------------------------------")

# Get target IP from user
target = input("Enter Target IP Address: ")

# Get port selection
print("\nSelect Port Scanning Option:")
print("1. Scan a single port")
print("2. Scan a range of ports")
print("3. Scan common ports")

choice = input("\nEnter your choice (1-3): ")

# Configure port selection
if choice == "1":

    port = int(input("Enter port number: "))
    ports = [port]

elif choice == "2":

    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range!")
        exit()

    ports = range(start_port, end_port + 1)

elif choice == "3":

    ports = [21, 22, 23, 25, 53, 80, 110,
             143, 443, 445, 3306, 3389, 8080]

else:
    print("Invalid selection!")
    exit()

# Display scan information
print("\n--------------------------------")
print("Target IP:", target)
print("Starting Scan...")
print("--------------------------------")

# Scan selected ports
for port in ports:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED/FILTERED] Port {port}")

    sock.close()

print("--------------------------------")
print("       SCAN COMPLETED")
print("--------------------------------")
