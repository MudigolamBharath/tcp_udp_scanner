
import nmap
scanner=nmap.PortScanner()
print("Welcome, this is a simple automation tool")
print("<---------------------------------------->")
ip_Addr=input("please enter the IP address you want to scan: ")
print("the IP you entered is: ",ip_Addr)
type(ip_Addr)
resp=input("""\nplease enter the type of scan you want to run
           1)SYN ACK Scan
           2)UDP Scan
           3)Comphrehensive scan\n""")
print("you have selected ",resp)
if resp == '1':
    print("Nmap version ",scanner.nmap_version())
    scanner.scan(ip_Addr,'1-1024','-vv -sS')
    print(scanner.scaninfo())
    print("ip status: ",scanner[ip_Addr].state())
    print(scanner[ip_Addr].all_protocols())
    print("open Ports ",scanner[ip_Addr]['tcp'].keys())
elif resp =='2':
    print("Nmap version ",scanner.nmap_version())
    scanner.scan(ip_Addr,'1-1024','-vv -sU')
    print(scanner.scaninfo())
    print("ip status: ",scanner[ip_Addr].state())
    print(scanner[ip_Addr].all_protocols())
    print("open Ports ",scanner[ip_Addr]['udp'].keys())
elif resp=='3':
    print("Nmap version ",scanner.nmap_version())
    scanner.scan(ip_Addr,'1-1024','-vv -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("ip status: ",scanner[ip_Addr].state())
    print(scanner[ip_Addr].all_protocols())
    print("open Ports ",scanner[ip_Addr]['tcp'].keys())
else :
    print("please enter a valid option")
