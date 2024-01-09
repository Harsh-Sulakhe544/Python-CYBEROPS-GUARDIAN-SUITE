import ctypes

class ConsoleColorManager:
    # Constants for color codes
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

    # use of constructors 
    def __init__(self):
        # Initialize default console colors
        self.default_foreground = self.FOREGROUND_RED | self.FOREGROUND_GREEN | self.FOREGROUND_BLUE
        self.default_background = self.BACKGROUND_BLACK
        self.set_console_color(self.default_foreground, self.default_background)

    # change the default console col0r - for Enter text color 
    def set_console_color(self, foreground, background):
        ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), foreground | background)

    # this will reset the console after i/p 
    def reset_console_color(self):
        self.set_console_color(self.default_foreground, self.default_background)
    
    # this will set the color based on user 
    def change_console_color(self, color_code):
        color_mapping = {
            'black': self.BACKGROUND_BLACK,
            'red': self.BACKGROUND_RED,
            'green': self.BACKGROUND_GREEN,
            'yellow': self.BACKGROUND_RED | self.BACKGROUND_GREEN,
            'blue': self.BACKGROUND_BLUE,
            'magenta': self.BACKGROUND_RED | self.BACKGROUND_BLUE,
            'cyan': self.BACKGROUND_GREEN | self.BACKGROUND_BLUE,
            'white': self.BACKGROUND_RED | self.BACKGROUND_GREEN | self.BACKGROUND_BLUE,
            'pink': self.BACKGROUND_PINK,  
            'purple': self.BACKGROUND_PURPLE,  
            'golden': self.BACKGROUND_YELLOW,  
            'violet': self.BACKGROUND_VIOLET, 
        }

        # traverse the dict above 
        if color_code in color_mapping:
            # us self to call the function 
            self.set_console_color(self.FOREGROUND_RED | self.FOREGROUND_GREEN 
                | self.FOREGROUND_BLUE, color_mapping[color_code])
            
            # convert the values of dict to a list to ease of access , color code is red, blue 
            # access the index() of color that we want 
            
            # [ => start of a new escape sequence , m means end of escape sequence 
            print(f"\033[1;37;{40 + list(color_mapping.values()).index(color_mapping[color_code])}mChanging console color to {color_code}!")
            
        else:
            # Background-color-ascii-code => 40 + foreground-color-ascii  
            # 1 is bold , 37 - white foreground
            
            print("\033[1;37;40m Invalid color code. Available colors: black, red, green, yellow, blue, magenta, cyan, white, violet, golden, purple, pink")