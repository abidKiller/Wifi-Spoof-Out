
import os 
import sys
import time


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

def heading():
  
   spaces = " " * 76
   sys.stdout.write(Color.RED + spaces + """
 @@@  @@@  @@@ @@@ @@@@@@@@ @@@   @@@@@@ @@@@@@@   @@@@@@   @@@@@@  @@@@@@@@   @@@@@@  @@@  @@@ @@@@@@@
 @@!  @@!  @@! @@! @@!      @@!  !@@     @@!  @@@ @@!  @@@ @@!  @@@ @@!       @@!  @@@ @@!  @@@   @@!  
 @!!  !!@  @!@ !!@ @!!!:!   !!@   !@@!!  @!@@!@!  @!@  !@! @!@  !@! @!!!:!    @!@  !@! @!@  !@!   @!!  
  !:  !!:  !!  !!: !!:      !!:      !:! !!:      !!:  !!! !!:  !!! !!:       !!:  !!! !!:  !!!   !!:  
   ::.:  :::   :    :       :    ::.: :   :        : :. :   : :. :   :         : :. :   :.:: :     :   
    """ +Color.END + Color.BLUE +
    '\n' + '{}Kick unwanted devices from wifi{}'.format(Color.YELLOW,Color.RED,Color.YELLOW,Color. BLUE).center(120)+
    '\n'+'Creator: {}abidkiller({}Abid Ahsan Samin{}{})'.format(Color.RED,Color.BLUE,Color.END,Color.RED).center(128))

def menu():
   print('\nChoose an option from the menu:\n')
    
   print('\t\t{}[{}O{}]{} Spoof out {}ONE{} device'.format(Color.YELLOW,Color. RED, Color.YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))
   
   print('\t\t{}[{}M{}]{} Spoof out {}MULTIPLE{} devices'.format(Color.YELLOW,Color. RED, Color.YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))
   
   print('\t\t{}[{}A{}]{} Spoof Out {}ALL{} devices'.format(Color.YELLOW,Color. RED,Color. YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))

   print('\t\t{}[{}L{}]{} Spoof Out {}Limit ONE{} device'.format(Color.YELLOW,Color. RED,Color. YELLOW,Color. WHITE,Color.GREEN,Color.WHITE))

   print('\n\t\t{}[{}E{}]{} Exit\n'.format(Color.YELLOW, Color.RED, Color.YELLOW, Color.WHITE))

def scanningAnimation(text):
    try:
        global stopAnimation
        i = 0
        while stopAnimation is not True:
            tempText = list(text)
            if i >= len(tempText):
                i = 0
            tempText[i] = tempText[i].upper()
            tempText = ''.join(tempText)
            sys.stdout.write(GREEN + tempText + '\r' + END)
            sys.stdout.flush()
            i += 1
            time.sleep(0.1)
    except:
        os._exit(1)