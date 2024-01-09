# main file - 1  (NOTE : DELETE THE PY_CACHE FILE , BCUZ IT WILL COMPILE EVERY FILE SEPARATELY)
# for this if u type 1 => then press Enter 
import os
import backdoor
import directories
import Ping
import Portinfo
import keylogger
import EncryptDecrypt
import CerditCardValidator
import change_color
import INFO  # to get whole system info
import ToDoApp #it is a whole applications
import socket
import requests
import getpass

print(" ` [ ]  \  \  | , .  ~ ! @ # $ % ^ & * ( ) _ + { } : ; < > \n \n WELCOME TO CYBEROPS GUARDIAN SUITE \n \n  ! @ # $ % ^ & * ( ) _ + { } : ; < > ~ ` [ ]  \  \  | , .  \n \n ")

# avoid the default start for the key-logger 
keylogger_started = False

def is_host_up(url):
    try:         
        parts = url.split('/') 
        # print(parts)
        
        # Validate the IP address
        ip_part = parts[0]  # Assuming the host is at index 2 in the URL (e.g., http://example.com/...)
        ip_part = str(ip_part)
        
        socket.create_connection((ip_part, 80), timeout=2)
        print(f"The host {ip_part} is reachable.")
        return True
        
    except (socket.timeout, socket.error):
        print(f"The host {ip_part} is not reachable.")
        return False 
    
def validate_url(url):
    return url.startswith('http')  and 'dvwa' in url and url.endswith('login.php') 

    
def validate_username(username):
    return username == "admin" and isinstance(username, str)

def validate_password_file(password_file):
    _, password_extension = os.path.splitext(password_file)
    return password_extension.lower() == '.txt'

def validate_login_failed_string(login_failed_string):
    return bool(login_failed_string)

def validate_target_url(target_url):
    return bool(target_url) and isinstance(target_url, str)

def validate_directory_file(file_name):
    _, file_extension = os.path.splitext(file_name)
    return bool(file_name) and file_extension.lower() == '.txt'

# Function to receive input until all validations are successful
def get_valid_input(prompt, validation_function, error_message, file_check=False):
    while True:
        user_input = input(prompt)
        if file_check and not os.path.isfile(user_input):
            print(f"the file {user_input} doesn't exist please enter a valid file")
        if validation_function(user_input):
            return user_input
        else:
            print(error_message)

# for 2nd choice 
def validate_file(file_name):
    if not os.path.exists(file_name):
        print("file does not exisits ")
        file_name = input("Enter the file name once again : ")
        
        # to check for multiple times for correct file 
        if not validate_file(file_name) :
            return validate_file(file_name)
        
        return file_name
    
    # but if already file exists , dont do anything 
    else:
        return file_name

# lock for waste inputs , only integer is accepted , and displayed  
def get_integer_input(prompt):
    while True:
        try:
            user_input = getpass.getpass(prompt)
            if user_input: 
                result = int(user_input)  # Try to convert to integer
                print(result)
                return result
        
        except ValueError:
            print("\n \n Invalid input. Please enter an integer.")
               

#  START THE KEYLOGGER WHEN REQUIRED , so use format()

choice = None
while not isinstance(choice, int):

        # Keyboard lock functionality

    choice = get_integer_input('''Enter your choice : 
                   1.To Hack the PassWord for A Website 
                   2.To Check All the Directories from a Specific URL 
                   3.Enter Website name to ping 
                   4.To Scan Required Ports and fetchy info
                   5.Toggle keyLogger (currently {})
                   6.Encrypt Decrypt 
                   7.Credit Card Validator
                   8.Color with terminal 
                   9.want some SYSTEM INFO
                   10.To Manage all your tasks
                   11.exit \n '''
                   .format("ON" if keylogger_started else "OFF"))

# todo KEYBOARD LOCK FOR WASTE INPUTS 
if choice == 1:
    print("\n ?????!!!!@@  WELCOME TO PASSWORD CRACKER !!!!@@??????")
    url = get_valid_input('[+] Enter Page URL: ', validate_url, "URL should start with http:// ,and it should have dvwa in the url  and it should have login.php at the end ")
    
    try:
        # Split the URL by "//" to get the part after "http://" or "https://"
        without_protocol = url.split("//")[1]

        # Split the remaining part by "/" to get the IP address or domain
        ip_or_domain = without_protocol.split("/")[0]

        # Construct a new URL with just the IP address
        ip_url = f"http://{ip_or_domain}/"

        # Make a request to check if the host is up
        response = requests.get(ip_url)
        response.raise_for_status()  # Raises HTTPError for bad responses

        print(f"The host {ip_url} is up and running.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}. The host {url} is not reachable.")
        exit(0)
    
            
    username = get_valid_input('[+] Enter Username For The Account To Bruteforce: ', validate_username,
                               "Username should be 'admin' and must be a string.")

    password_file = get_valid_input('[+] Enter Password File To Use: ',validate_password_file,
                                    "Password file must have a .txt extension.",    file_check=True)

    # user can give input as s -> it will fail , cuz response is Welcome from the metasploitable ip, 
    #  when we login in 
    login_success_string = "Welcome"
    
    cookie_value = input('Enter Cookie Value (Optional): ')

    print("ALL INPUT FIELDS ARE VALID")
    
    with open(password_file, 'r') as passwords:
        # remove the line-whitespaces , using list-comprehension 
        password_list = [line.strip() for line in passwords]

    backdoor.cracking(username,url, password_list, cookie_value, login_success_string)
            
    print('[!!] Password Not In List')

# todo validation 
elif choice == 2:
    print("\n &&&&&&&&& WELCOME TO DIRECTORY SEARCH &&&&&&&&&&&& \n")
    target_url = input('[*] Enter Target URL  (Dont start with http:// it is already set by default): begin with pure number like Y.Y.Y.Y/dir/subdir : ')
        
    if not is_host_up(target_url):
        exit(0)
    
    url= directories.is_valid_url(target_url)
    print(url)
    
    file_name = input('[*] Enter Name Of The File Containing Directories: ')
    file_name= validate_file(file_name)
    file_directory_extension = os.path.splitext(file_name)   # split the file.txt => (file ,.txt)
    # print(file_directory_extension)
    flag = 1
    
    # take only the directories you want dont search whole list 
    z = int(input("Enter the number of directories you want to discover for the current url "))
    
    if not target_url or (type(target_url) != str):
        print("Target URL is mandatory to scan the URL and fetch all its sub-Directories")
        flag = 0     
        
    if not file_name or file_directory_extension[1] != '.txt':
        print(" NOTE:  .txt is the extension that should be used to scan list of Directories ")
        flag = 0
    
    # set a counter for to stop printing url after desired times 
    counter = 0    
    
    file = open(file_name, 'r')
    for line in file:
        directory = line.strip()
        full_url = target_url + '/' + directory
        response = directories.request(full_url)
        # print(response)
                
        # by default if success -- 200
        if response:
            print(' \n [*] Discovered Directory At This Path: ' + full_url)
        
        counter += 1    
        if counter >= z:
            print("\n Reached the required number of urls specified ")
            break
        
    # todo validation 
elif choice == 3:
    print("\n *******  PING THE DOMAIN NAME FOR ANY WEBSITE \n (EXAMPLE : google.com)  ********* \n")
    url_to_ping = input("Enter the url/domain(ip) to ping : ")
    Ping.ping_website(url_to_ping, flag=1)
    
    
elif choice == 4:
     
    print("\n *HOST**  SCAN THE NETWORKING PORT FOR ANY MACHINE YOU WANT  **IP** \n")
    target_ip = input("Enter the target IP address: ")
        
    if not is_host_up(target_ip):
        exit(0)
        
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    # scan tcp protocols 
    open_ports = Portinfo.scan_ports(target_ip, start_port, end_port)

    final_result = Portinfo.print_results(open_ports) 

elif choice == 5:
    # it will create output.txt => when u run this choice 
    # w- write mode ==> if file does not exists , it will create output.txt and then add  the keys 
    print(" \n qwerty  WELCOME TO KEYLOGGER --------------- asdfgh  \n")
    with open(keylogger.output_file_path, 'w') as f:
        pass
    
# Start the keylogger, only when required --> remaining key-logger functions will execute automatically
    keylogger.start_keylogger()
        
elif choice == 6:
    print("\n ~!@#$%^&*()_+  WELCOME TO ENCRYPTOR AND DECRYPTOR  ~!@#$%^&*()_+ \n ")
    text = input("Enter the text : ")    
    # Generate cipher key
    cipher_key = EncryptDecrypt.generate_cipher_key()
    
        # Encryption
    cipher_text = EncryptDecrypt.encrypt(text, cipher_key)
    print("\n Text  : " + text)
    print("\n Cipher Key: " + str(cipher_key))
    print("\n Cipher: " + cipher_text ) 
    
        # Decryption back to user-normal format - text
    decrypted_text = EncryptDecrypt.decrypt(cipher_text, cipher_key)
    print("\n Decrypted Text: " + decrypted_text)
      
elif choice == 7:
    print("\n $$$$$$$$$$ WELCOME TO CREDIT CARD VALIDATOR $$$$$$$$$$ \n ")
    credit_card_no = input("Enter your Credit Card Number in 16bit format to check whether is it Valid or not : ")
    is_valid = CerditCardValidator.validate_credit_card(credit_card_no)
    if not is_valid:
        print("Your Credit Card number is not valid ")
    else:
        print("Your Credit Card number is valid ")
    
elif choice == 8:
    # USING OOPS 
    print("\n !#$%^ ##### WELCOME TO COLOR MANAGER #### )(*&^) \n")
    
    console_color_manager = change_color.ConsoleColorManager()    
    # By default, the following line should look dark
    color_code = input("\033[1;37;40mEnter the color code: ").lower()
    console_color_manager.change_console_color(color_code)
    
    # Do your other operations here
    
    input("Press Enter to reset console color...")
    console_color_manager.reset_console_color()
    
elif choice == 9:
    # using OOPS => 
    
    # obj = module.className  , then 
    # obj.method() 
    
    print(" \n ^^##root@system >> WELCOME TO SYSTEM MANAGER  \n")
    system_info_object = INFO.SystemInformation()   
    system_info = system_info_object.get_system_info()
    
    # Print formatted system information in key value pair using items()
    for key, value in system_info.items():
        # find for network-card , and hotfix as key 
        
        if key == "Network Card(s)":
            print(f"{key}:")
            
            for card in value:
                print(f"  {card['Connection Name']}:")
                print(f"    DHCP Enabled: {card['DHCP Enabled']}")
                print(f"    IP address(es): {', '.join(card['IP address(es)'])}")
                
        elif key == "Hotfix(s)":
            print(f"{key}:")
            # number of hotfixs installed may depend on SYSTEM 
            
            # fetch only the values form the just-above for loop 
            for hotfix in value:
                print(f"  [Hotfix ID: {hotfix[0]}, Description: {hotfix[1]}, Installed on: {hotfix[2]}]")
  
        else:
            print(f"{key}: {value}")
    
elif choice == 10:
    print("????+++---^^ TODO - APP ????+++---^^^")
    final = ToDoApp.main()
    
elif choice == 11:
    print("----------- THANKS FOR USING , VISIT AGAIN ---------")
    exit(0)    