import socket

def scan_ports(domain):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portstoscan = [22, 25, 53, 70, 80, 113]

    socket.gethostbyname(domain)
    print("Starting scan on: ", domain)

    for port in portstoscan:
        result = single_scan(domain, port)
        if result == True:
            print(f'Port {port} is open.')
        else:
            print(f'Port {port} is closed.')  

def single_scan(domain, port):
    try: 
        s.connect((domain, port))
        return True
    except:
        return False
