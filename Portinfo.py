# 5 
# using SOCKET-Programming for ports 
import socket

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name 
    except socket.error:
        return "Unknown"
    
def scan_ports(ip, start_port, end_port):
    # CREATE A LIST 
    open_ports = []

    for port in range(start_port, end_port + 1):
        # AF_INET - use ipv4 , SOCK_STREAM - means use TCP-protocol (not udp --> slower )
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # consider 1 sec for each socket operation to happen, >1 sec - error   

    # If connect_ex returns 0, it means the connection was successful, indicating that the port is open
        result = sock.connect_ex((ip, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports

def print_results(open_ports):
    
    if open_ports:
        # using string format , <10 => fit the values towards leftside(ex 10px) , 
        # <15 means => example just 15 px of width for that state 
        print("{:<10} {:<15} {}".format("PORT", "STATE", "SERVICE"))
        
        for port in open_ports:       
            service  = get_service_name(port)
            print("{:<10} {:<15} {}".format(port , "open", service))
    else:
        print("No open ports found.")