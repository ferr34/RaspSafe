# Script for the main menu 

import os 
import datetime

choice = 0

def show_menu():
    print("Options available: ")
    print("1. List all the files in the safe")
    print("2. Add a file in the safe")
    print("3. Delete permantently a file from the safe")
    print("4. Unsafe a file from the safe")
    print("5. Exit from the safe")
    
    choice = input("Please choose an option: ")


# Input type check 
while True: 
    if not str(choice).isdigit():
        # Error - need to reinsert 
        show_menu()
    else: 
        break


# Input correct, going to script for every function
match choice:
    case 1:
        print("Calling the method...")
    case 2:
        print("Calling the method...")
    case 3: 
        print("Calling the method...")
    case 4:
        print("Calling the method...")
    case 5:
        print("Calling the method...") 
    




