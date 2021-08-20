
import os 
import sys
import time
import cursor

global stop_animation
stop_animation=False
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ORANGE = '\033[33m'
    WHITE = '\33[97m'
    END = '\033[0m'


class PrintUtils:
    def __init__(self):
        self.stop_animation=False
        
    def heading():

        

        spaces = " " * 76
        sys.stdout.write(Color.RED + spaces + """
            
    ██╗    ██╗██╗███████╗██╗   ███████╗██████╗  ██████╗  ██████╗ ███████╗   ██████╗ ██╗   ██╗████████╗
    ██║    ██║██║██╔════╝██║   ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝  ██╔═══██╗██║   ██║╚══██╔══╝
    ██║ █╗ ██║██║█████╗  ██║   ███████╗██████╔╝██║   ██║██║   ██║█████╗    ██║   ██║██║   ██║   ██║   
    ██║███╗██║██║██╔══╝  ██║   ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝    ██║   ██║██║   ██║   ██║   
    ╚███╔███╔╝██║██║     ██║   ███████║██║     ╚██████╔╝╚██████╔╝██║       ╚██████╔╝╚██████╔╝   ██║   
     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝   ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝        ╚═════╝  ╚═════╝    ╚═╝   
            """ +Color.END + Color.BLUE +
            '\n' + '{}Kick unwanted devices from wifi{}'.format(Color.YELLOW,Color.RED,Color.YELLOW,Color. BLUE).center(120)+
            '\n'+'Creator: {}abidkiller({}Abid Ahsan Samin{}{})'.format(Color.RED,Color.BLUE,Color.END,Color.RED).center(128))

    def menu():

    
        
        print('\nChoose an option from the menu:\n')
            
        print('\t\t{}[{}O{}]{} Spoof out {}ONE{} device'.format(Color.GREEN,Color. RED, Color.GREEN,Color. YELLOW,Color.RED,Color.YELLOW))
        
        print('\t\t{}[{}M{}]{} Spoof out {}MULTIPLE{} devices'.format(Color.GREEN,Color. RED, Color.GREEN,Color. YELLOW,Color.RED,Color.YELLOW))
        
        print('\t\t{}[{}A{}]{} Spoof Out {}ALL{} devices'.format(Color.GREEN,Color. RED,Color. GREEN,Color. YELLOW,Color.RED,Color.YELLOW))

        print('\t\t{}[{}L{}]{} Spoof Out {}Limit ONE{} device'.format(Color.GREEN,Color. RED,Color. GREEN,Color. YELLOW,Color.RED,Color.YELLOW))

        print('\n\t\t{}[{}E{}]{} Exit\n'.format(Color.GREEN, Color.RED, Color.GREEN, Color.YELLOW))
        



    def scanning_animation(self,text):
        global stop_animation
        try:
            animation = ["■ □ □ □ □ □ □ □ □ □ □ □ □",
                         "■ ■ □ □ □ □ □ □ □ □ □ □ □", 
                         "■ ■ ■ □ □ □ □ □ □ □ □ □ □", 
                         "■ ■ ■ ■ □ □ □ □ □ □ □ □ □", 
                         "■ ■ ■ ■ ■ □ □ □ □ □ □ □ □", 
                         "■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □", 
                         "■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □", 
                         "■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □", 
                         "■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □",
                         "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □",
                         "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □",
                         "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □",
                         "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■"]

            dummy="Runnin,Please Wait!"
            cursor.hide()
            sys.stdout.write('{}{}{}'.format(Color.YELLOW,text,dummy))
            i=0
            length=len(animation)
            stop_animation=False
            reverse=False
            
            while stop_animation==False:
                
                reverse = True if i==length-1 else (False if i==0 else reverse)

                time.sleep(0.2)
               
                
                sys.stdout.write("\r" + '{}{}'.format(Color.YELLOW,animation[i % len(animation)]))
                sys.stdout.flush()

                i= (i-1 if reverse else i+1)
               
                        

            sys.stdout.write("\x1b[1A\x1b[2K")
            
            
            sys.stdout.write('\r'+text+' DONE..!'.format(Color.GREEN)) 
         
           
                
        except:
            os._exit(1)
