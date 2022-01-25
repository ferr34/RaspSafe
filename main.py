# RaspSafe - A safe for your data on a Raspberry Pi4

# Author @ferr_34
import signal
from bin import encrypt as enc
from bin import first_time as ft
from bin import access as acc
import time
import os
import sys

# Step 0 - Accessing the Safe
print('__________                        _________       _____       ')
print('\______   \_____    ____________ /   _____/____ _/ ____\____  ')
print('|       _/\__  \  /  ___/\____ \\_____  \\__  \\   __\/ __ \ ')
print('|    |   \ / __ \_\___ \ |  |_> >        \/ __ \|  | \  ___/ ')
print('|____|_  /(____  /____  >|   __/_______  (____  /__|  \___  >')
print('        \/      \/     \/ |__|          \/     \/          \/ ')

print('Made by @ferr34 - www.github.com/ferr34')

def access_safe():
    key2 = ""
    acc.access_safe_menu(key2)
    

def setup():
    # Step 1: First time of using the safe
    file_check = open("utilities/firstTime.txt","r").read()

    if file_check == "":
        # Empty file, first time
    
        # Writing the file with a simple character
        file_check = open("utilities/firstTime.txt","a")
        file_check.write("ok")
        file_check.close()
    
        ft.first_time()
    else:
        # No first time
        print('The safe is already set up. Accessing the safe...')
        access_safe()

while True:
    print('1) Access the safe')
    print('2) Set up your safe')
    print('3) Exit from the program.')
    
    choice = input('Digit an option:')
    
    if choice == 1:
        access_safe()
    
    if choice == 2:
        setup()
    
    if choice == 3:
        # Exit from the safe
        sys.exit('Leaving the safe... Bye!')
