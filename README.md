# Programa de Escaneo de Puertos
Este es un programa de Python que utiliza la biblioteca nmap para escanear puertos abiertos en una determinada dirección IP o rango de direcciones IP. El programa devuelve los puertos abiertos en formato JSON.

Requisitos
Antes de ejecutar el programa, asegúrate de tener los siguientes requisitos:

Python instalado en tu sistema.
La biblioteca nmap instalada. Puedes instalarla ejecutando el siguiente comando en tu terminal:
bash
Copy code
pip install python-nmap
Funcionamiento
El programa utiliza la biblioteca nmap para realizar el escaneo de puertos. La función principal es get_open_ports, que toma como parámetro la dirección IP o rango de direcciones IP que se desea escanear. Devuelve un diccionario que contiene las direcciones IP como claves y una lista de puertos abiertos como valores.


def get_open_ports(target):
    scanner = nmap.PortScanner()
    
    scanner.scan(target, arguments='-p- --open')
    
    open_ports = {}
    
    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            open_ports[host] = list(ports)
            
    return open_ports
El programa utiliza el objeto PortScanner de la biblioteca nmap para realizar el escaneo. Se configura con el rango de puertos -p- y la opción --open para buscar puertos abiertos. Luego, itera sobre todos los hosts encontrados y recopila la información de los puertos abiertos en cada uno.

Después de llamar a la función get_open_ports, se imprime en la consola la lista de puertos abiertos en formato JSON utilizando la función json.dumps para una mejor presentación.

target_host = '192.168.20.1-254'
open_ports = get_open_ports(target_host)

print(f"Los puertos abiertos en {target_host} son:")
print(json.dumps(open_ports, indent=4))

En este ejemplo, se escanea el rango de direcciones IP de 192.168.20.1 a 192.168.20.254. Los puertos abiertos encontrados se muestran en la consola en formato JSON con sangría para una mejor legibilidad.

Ejecución
Para ejecutar el programa, asegúrate de haber cumplido con los requisitos mencionados anteriormente y guarda el código en un archivo con la extensión .py. Luego, puedes ejecutar el programa ejecutando el siguiente comando en tu terminal:

python nombre_del_archivo.py

Reemplaza nombre_del_archivo.py con el nombre de tu archivo Python. El programa comenzará a escanear los puertos y mostrará los resultados en la consola.
