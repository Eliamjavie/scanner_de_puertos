import nmap
import json

def get_open_ports(target):
    scanner = nmap.PortScanner()
    
    scanner.scan(target,
                 arguments='-p- --open')
    
    open_ports = {}
    
    for host in scanner.all_hosts():
        
        for proto in scanner[host].all_protocols():
            
            ports = scanner[host][proto].keys()
            open_ports[host] = list(ports)
            
    return open_ports


target_host = '192.168.20.1-254'
open_ports =get_open_ports(target_host)


print(f"Los puertos abiertos en {target_host} son:")

print(json.dumps(open_ports,indent=4))
