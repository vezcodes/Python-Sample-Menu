# A sample code by Vez Codez
# http://vezcodez.c1.biz

import os

from colorama import Fore
from time import sleep

# DEFINING THE COLORS

green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
black = Fore.BLACK
white = Fore.WHITE 
magenta = Fore.MAGENTA

# You can change this to anything you want to :3
banner = blue + f'''
            
        ░██████╗░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗
        ██╔════╝██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝
        ╚█████╗░███████║██╔████╔██║██████╔╝██║░░░░░█████╗░░
        ░╚═══██╗██╔══██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░
        ██████╔╝██║░░██║██║░╚═╝░██║██║░░░░░███████╗███████╗
        ╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝
                        by Vez Codez
                        
'''

# <><><> PUT HERE YOUR FUNCTIONS

def Test1():
    os.system('cls')
    print(banner)
    print(green + 'Successfully loaded the Test1 function!')
    input(cyan + 'Press the ENTER key to return to the menu. . .')
    sleep(1)
    main()

def Test2():
    os.system('cls')
    print(banner)
    print(green + 'Successfully loaded the Test2 function!')
    input(cyan + 'Press the ENTER key to return to the menu. . .')
    sleep(1)
    main()

# <><><> STOP HERE WITH YOUR FUNCTIONS

def main():
    # This functions clears the console's screen
    os.system('cls') # CLS is used for windows operating systems

    # You can change this to anything you want aswell,!!!!!!!!!!!! [ but make sure to change the variables and functions!! ] !!!!!!!!!!
    menu = f'''
    {yellow}[{white}1{yellow}]{cyan} Test 1
    {yellow}[{white}2{yellow}]{cyan} Test 2
    {yellow}[{white}3{yellow}]{red} Exit
    '''

    # This here, yes this, prints (shows) the variables [ BANNER ] and [ MENU ]

    print(banner)
    print(menu)

    # This gives the user the ability to choose an option from the menu

    option = input(f'{yellow}[{white}>{yellow}]{cyan} Select: ')

# This is the code to go to the functions

    # This here goes to the Test1 function
    if option == "1":
        print(cyan + 'Loading. . .')
        sleep(2)
        Test1()

    elif option == "2":
        print(cyan + 'Loading. . .')
        sleep(2)
        Test2()
    
    # This function down below exits the program.
    elif option == "3":
        print(yellow + "Goodbye :D")
        sleep(1)
        quit()

    # This function is trying to fetch a wrong choice which is not defined in the menu. If it fetched the wrong choice, it'll reset the console's screen.
    else:
        print(red + "[!] Invalid choice!")
        sleep(2)
        main()
    main()





if __name__ == '__main__':
    main()
else:
    print(red + "[!] An error occured!\nRetrying...")
    sleep(1)
    main()
