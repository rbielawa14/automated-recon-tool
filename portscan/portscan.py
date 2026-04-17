import socket

''' Pseudocode: 
function scan_ports(target_ip, ports_list):
    open_ports = []
    for port in ports_list:
        create socket with timeout
        try to connect to target_ip:port
        if connection succeeds:
            add port to open_ports
        close socket
    return open_ports
'''