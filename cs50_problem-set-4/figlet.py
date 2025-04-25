import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in list:
            s = input("Input: ")  
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(s))
        else:
            sys.exit()      
    else:
        sys.exit()

elif len(sys.argv) == 1:
    s = input("Input: ")  
    figlet.setFont(font = random.choice(list))
    print(figlet.renderText(s))
else:
    sys.exit()