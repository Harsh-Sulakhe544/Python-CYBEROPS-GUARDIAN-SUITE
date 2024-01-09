#  3 CODE 
# this code is under test for different test cases in new.py file 
import socket
import requests

def request(url):
    try:
        if is_valid_url(url):
            return requests.get("http://" + url)
        else:
            print(f"Invalid IP address: {url}")
    except requests.exceptions.ConnectionError:
        pass

# THIS IS TESTING CODE -- CHECK THE directories.py FILE -- IT WORKS , but not for all test-cases, 
# so it is TESTING FILE FOR DIRECTORIES.PY

def is_valid_url(user_input):
    parts = user_input.split('/')
    # print(parts)
    if len(parts) < 1:
        return "Invalid URL format. It should have at least an IP address."

    # Validate the IP address
    ip_part = parts[0]
    ip_components = ip_part.split('.')
    
    if len(ip_components) != 4 or not all(component.isdigit() and 0 <= int(component) <= 255 for component in ip_components):
        return "Invalid IP address format. Each part of the IP should be a number between 0 and 255."

    # Check if there are directories after the IP address
    if len(parts) > 1:
        # Validate the rest of the components (directories)
        for component in parts[1:]:
            if not(all(char.isalpha() or char == '.'  for char in component)):
                return f"Invalid directory: {component}. It should consist only of letters."

    return "Valid URL format."

def get_valid_ip_from_user(user_input):
    flag = 1
    while True:
        if flag == 1:
            return is_valid_url(user_input)
        
            
        