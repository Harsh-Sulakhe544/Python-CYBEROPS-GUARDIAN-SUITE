<!-- Concepts you will learn during this project --> 
Recursion 
Working with LIST, DICTIONARY, TUPLES
INTERCONVERSION OF DATATYPES 
Comprehensions , (list, dictionary )
how to link 1 python file with another 
file i/o operations , different modes to open a file = (a , w , r )
Exception handling 

why pycache - faster --> c- compliling 

how to ping a network 
how to attack a virtual machine =- metasploitable 2
keyLogger -> how to set an application on or off 
how to encrypt and decrypt the text 
Basic working of  log files with python 
Credit-Card validation Algo 
Change Color of System Console 
SystemInfo - complete system 


WORKING WITH PYTHON MODULES 

os 
request 
socket
pyinput, keyboard, mouse 
termcolor 
logging 
time
random
string
logging
ctypes - windows color console 
subprocess - main API for to run command in form of process 
system-info ==> to deal mainly with hotfixes(quick-recovery-software program )

Built-in-functions used

int(), float(), bool() , print(), input() , range(n+1) -> 0 to n
time() - current time , sleep() -> to stop for a certain time 

socket.create_connection((ip,port-no))
socket.gethostbyname(host)

exit() - break the whole program   
any() - takes a tuple 
endswith('req-string'), startswith('req-string')
split('.') -> string to list 

min(), max() => preprocessing functions 

isinstance(5, int) - True
settimeout(5) 
format("PORT", "STATE", "SERVICE")
getservbyport(port)

shuffle()
list(), dict(), zip(a,b)=> (a,b)
get() -> to avoid errors 
_exit(1)
len(), all(ele.isdigit())
open(), write(), join()-> list to string 
items() -> to get both the keys and values of dictionary

StreamHandler(),  # Log to console(in terminal )
FileHandler('credit_card_validator.log')  # Log to file

x = map(myfunc, ('apple', 'banana', 'cherry')) -> func is a function , each item is sent to myfunc
filter(str, 'a) -> a is str 
reverse() - to reverse a list 
sum() - to add all 
append() - apply at the end 
enumerate() - auto increment x = ('apple', 'banana', 'cherry')  , y = enumerate(x)

logging.info(), logging.error(), logging.warning()
logging.getLogger().getEffectiveLevel() , level ->  warning (by default), 
getLogger() -> to create logger and call debug(), info(), warning(), error(), and critical() - system 
functions 

getsysteminfo()
run_command(x) => to run the system command x, 
ex : wmic qfe list brief - windows management instrumentation command  --> to show  hotfix detail info

basic info about : 
Network-cards ? -> LAN Adapter or network interface card => allows comuter to connect computer overa 
computer network 

DHCP (Dynamic Host configuration Protocol) -> is a network protocol that is used to configure network 
devices to communicate on an IP network. A DHCP client uses the DHCP protocol to acquire configuration 
information, such as an IP address, a default route, and one or more DNS server addresses from a DHCP 
server.

why subprocess.PIPE? 
Using subprocess.PIPE allows you to interact with the input, output, and error streams of a subprocess 
from your Python script. It's a way to establish communication channels between your script and the 
external process you're runnin

windows color constants for the console 

    FOREGROUND_BLACK = 0x0000
    FOREGROUND_GREEN = 0x0002
    FOREGROUND_RED = 0x0004
    FOREGROUND_BLUE = 0x0001
    FOREGROUND_INTENSITY = 0x0008
    BACKGROUND_BLACK = 0x0000
    BACKGROUND_GREEN = 0x0020
    BACKGROUND_RED = 0x0040
    BACKGROUND_BLUE = 0x0010
    BACKGROUND_INTENSITY = 0x0080
    BACKGROUND_YELLOW = 0x0060  
    BACKGROUND_PINK = 0x00C0  
    BACKGROUND_PURPLE = 0x0050  
    BACKGROUND_VIOLET = 0x0090  

working of windows cytpes with kernel : 
what is this below ? 
ex: ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 
foreground | background)

ctypes.windll.kernel32.GetStdHandle(-11): This part retrieves the standard output handle for the 
console. The parameter -11 represents STD_OUTPUT_HANDLE. It essentially gets a handle to the console 
window.

ctypes.windll.kernel32.SetConsoleTextAttribute(...): This part sets the text attributes of the console. 
It takes two arguments:

The first argument is the handle to the console obtained from GetStdHandle(-11).

The second argument is a combination of foreground and background colors. This is achieved by using the 
bitwise OR (|) operator to combine the foreground and background color values.

foreground | background: This is a bitwise OR operation that combines the foreground and background 
color values. The specific values for foreground and background are not provided in the code snippet you 
shared. You should replace foreground and background with the appropriate color values.

In Windows console programming, the colors are often represented using a combination of foreground and 
background attributes. For example, you might have foreground colors like FOREGROUND_RED, 
FOREGROUND_GREEN, etc., and background colors like BACKGROUND_BLUE, BACKGROUND_INTENSITY, etc. These 
values are combined using bitwise operations to set the desired text attributes.


Object Orientation programming : 

working with self 

how to use obj to connect to class from other file
obj = module.className  , then 
obj.method()

why use of yield -> The yield statement in the task_generator function is used to create a generator. A 
generator is a special type of iterable in Python that allows you to iterate over a potentially large 
sequence of data without loading the entire sequence into memory. Instead of returning all the values at 
once, a generator produces one value at a time and maintains its state between calls

why decorators ? ex : @function 
Decorators are often used for tasks such as logging, monitoring, caching, or other side effects.
*args and **kwargs => arguements and keyword-arguements 

python <--> json ? 
json.load() => to load the data from json file  
json.dump() => to convert anything kind of data to json => and write to json file

iterating over [{}, {}, {}] => using list comprehension

keyboard  lock => for only waste inputs (only integer is valid), and it is displayed 
if u press 1 => next press enter => to move forward