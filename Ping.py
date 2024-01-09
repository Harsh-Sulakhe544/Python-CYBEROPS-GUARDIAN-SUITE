# 4 
# used socket-programming , instead of run() 
# rtt - rounded trip time for the packet=> source->destination->source 
import socket
import time

def ip_valid(ip_address):
    # check for all domains using any (use tuples , not list )
    valid_suffixes = ('.com', '.in', '.org')
    if any(ip_address.endswith(valid_suffixes) for suffix in valid_suffixes):
        return True
    else: 
        while True:
            ip_address = input("Enter your Domain name again to ping :  ")
            # we want to validate only any-one of the things 
            if any(ip_address.endswith(suffix) for suffix in valid_suffixes):
                return ping_website(ip_address, flag=1)
            else: 
                print("Invalid Input , please try once again ")
    
def ping_website(host, flag):
    try:
        ip_address = socket.gethostbyname(host)
        print(f"TRY {ip_address} in your browser , REMEMBER it is not safe ")
        n = int(input("Enter number of packets(4-6) you want to ping for your domain : "))
        print(f"Pinging {ip_address} with {n*8} bytes of data:")

        sent_packets = 0
        received_packets = 0
        total_time = 0
        min_time = float('inf')
        max_time = 0

        for i in range(1, n+1):  # Sending n data packets
            start_time = time.time()
            try:
                # create the connection using port 80 for ip-address 
                socket.create_connection((ip_address, 80), timeout=5)
                end_time = time.time()
                ping_time = (end_time - start_time) * 1000  # Convert to milliseconds
                
                # why TTL ? -> Time to live (TTL) refers to the amount of time or “hops” that a packet 
                # is set to exist inside a network before being discarded by a router.
                
                print(f"Reply from {ip_address}: bytes=32 time={ping_time:.2f}ms TTL={i}")
                
                received_packets += 1
                total_time += ping_time  # average time for all recieved-packets 
                
                # preprocessing , considering the min and max among all data packets sent
                
                # min-time is set as - INFINITY , max-time =0  <== DEFAULT VALUES 
                min_time = min(min_time, ping_time)
                max_time = max(max_time, ping_time)
                
                flag = 1
                
            # gaierror : get-address information error , when host isn't found and  network-unreachable
            # it uses socket module to get info of host and port --here wrt time 
            except (socket.gaierror, socket.error) as e:
                print(f"Request timed out: {e}")
                flag = 0
                print("Something went wrong wait for some time ")
                ping_website(host, flag) 

            time.sleep(1)  # Wait for 1 second between packets
            sent_packets += 1

        # display the ping details 
        print("\nPing statistics:")
        
        print(f"    Packets: Sent = {sent_packets}, Received = {received_packets}, Lost = {sent_packets - received_packets} ({(sent_packets - received_packets) / sent_packets * 100:.0f}% loss),")
        
        if received_packets > 0:
            print(f"Approximate round trip times in milli-seconds:")
            print(f"    Minimum = {min_time:.2f}ms, Maximum = {max_time:.2f}ms, Average = {total_time / received_packets:.2f}ms")
        
        # if we recieved last packet(n) and got all info we want 
        if received_packets == n:
            exit(0)
               
    # check if it is not possible to ping 
    except (socket.gaierror, socket.error) as e:
        print(f"Error: {e}")
        print(f"Host '{host}' not found or unreachable.")  
        ip_valid(host)
        flag = 0       