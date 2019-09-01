#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

print('Hello, my name is Luca!')
menu = ' '
while (menu != 'end'):
    print('\n 1 - Favorite Game\n 2 - Concerns\n 3 - Excitements\n 4 - Stackoverflow\n 5 - Github\n')
    menu = input('What would you like to know about me? \n\n')
    menu = menu.strip().lower()
    if (menu == '1'):
        print('My favorite games are Borderlands and Pokemon.\n')
    elif (menu == '2'):
        print('I may have concerns about keeping up with unfamiliar programs, such as Godot.\n')
    elif (menu == '3'):
        print("Despite my worries, I'm still excited aboout possibly learning more about game languages and game development.\n")
    elif (menu == '4'):
        print("My stackoverflow.com number is 11981317.\n")
    elif (menu == '5'):
        print("My Github URL is https://github.com/LEDCat.\n")