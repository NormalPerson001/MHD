import nmap

scanner = nmap.PortScanner()

print("Hello this is my Nmap tool :) ")
print("==============================")

ip_a = input("Please Enter the IP address You Want: ")
print("the ip u entered"+ip_a)
type(ip_a)

res = input("""\nPlease enter the Type of Scan You want to run
               1)Aggressive Scan
               2)coming soon\n""")
print("you have selected option: ", res)

if res=='1':
    scanner.scan(ip_a,'0-65536', '-T4 -A')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_a].state())
    print(scanner[ip_a].all_protocols())
    print("Open Ports: ",scanner[ip_a]['tcp'].keys())
else:
    print("please enter a valid option")








