# Script for the main menu 

import os 
import datetime
import show_files as sf # External file for showing the file

choice = 0

def show_menu():
    print("Options available: ")
    print("1) List all the files in the safe")
    print("2) Add a file in the safe")
    print("3) Delete permantently a file from the safe")
    print("4) Unsafe a file")
    print("5) Exit from the safe")
    
    choice = input("Please choose an option: ")


# Input type check 
while True: 
    if not str(choice).isdigit():
        # Error - need to reinsert 
        show_menu()
    else: 
        break


# Input correct, going to script for every function
if choice == 1:
    user = input("Please insert username for search:")
    sf.show_tree(user)

if choice == 2:
    add_file()

if choice == 3: 
    delete_file()

if choice == 4: 
    unsafe_file()

if choice == 5: 
    print("See you soon. Leaving the safe...")
    exit()




