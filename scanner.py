import nmap

# Initialize the Nmap PortScanner object
scanner = nmap.PortScanner()

# Welcome message
print("Welcome! This is a simple Nmap automation tool")
print("<--------------------------------------------->")

# Get target IP address from user
ip_Addr = input("Please enter the IP address you want to scan: ")
print("The IP address you entered is:", ip_Addr)

# Get the type of scan the user wants to perform
resp = input("""
Please enter the type of scan you want to run:
    1) SYN ACK Scan
    2) UDP Scan
    3) Comprehensive Scan
Your choice: """)

print("You have selected option", resp)

try:
    if resp == '1':
        # SYN ACK Scan
        print("\n[+] Performing SYN ACK Scan...")
        print("Nmap version:", scanner.nmap_version())
        scanner.scan(ip_Addr, '1-1024', '-vv -sS')
        print(scanner.scaninfo())
        print("IP Status:", scanner[ip_Addr].state())
        print("Protocols:", scanner[ip_Addr].all_protocols())
        print("Open TCP Ports:", scanner[ip_Addr]['tcp'].keys())

    elif resp == '2':
        # UDP Scan
        print("\n[+] Performing UDP Scan...")
        print("Nmap version:", scanner.nmap_version())
        scanner.scan(ip_Addr, '1-1024', '-vv -sU')
        print(scanner.scaninfo())
        print("IP Status:", scanner[ip_Addr].state())
        print("Protocols:", scanner[ip_Addr].all_protocols())
        print("Open UDP Ports:", scanner[ip_Addr]['udp'].keys())

    elif resp == '3':
        # Comprehensive Scan
        print("\n[+] Performing Comprehensive Scan...")
        print("Nmap version:", scanner.nmap_version())
        scanner.scan(ip_Addr, '1-1024', '-vv -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("IP Status:", scanner[ip_Addr].state())
        print("Protocols:", scanner[ip_Addr].all_protocols())
        print("Open TCP Ports:", scanner[ip_Addr]['tcp'].keys())

    else:
        # Invalid option
        print("\n[!] Invalid option. Please enter 1, 2, or 3.")

except Exception as e:
    print("\n[!] An error occurred while scanning:")
    print(e)
