from Crypto.Hash import SHA256
import os
import sys
import datetime 
import time
from bin.menus import menu as mn
import encrypt as enc
import report as rp

def access_safe_menu(password):
    if password != "":
        # Password already read or first time, password chosen
        print('Password already read...')

        # Jumping to the menu 

    else:
        try_counter = 0
        while try_counter < 2:

            username = input("Username:")
            pass2 = input("Password: ")

            # Creating the access  key 
            access_key = username + '_' + pass2
    
            hash_one = SHA256.new()
            hash_one.update(access_key.encoding('utf-8'))
            update_file = open("utilities/hashes.txt","r").read()
        
            if update_file == hash_one:
                # User validated
                print('User authenticated. Welcome back.')
                
                # Opening the menu 
                mn.show_menu()

            else:
                # Error method - call to the report script
                print('Password not valid. Retry please.')
                today = datetime.date.today()
                rmc.send_alert(str(today.ctime()))

                rp.add_log(str(today.ctime))    

                try_counter = try_counter + 1
                
        if try_counter >= 3:
            # Safe needs to be ciphered 

            print('Too many attempts. The data will be now ciphered.')       
            enc.cipher_data()

            today = datetime.date.today()
            # Sending message 
            print('Safe ciphered. Bye.')

         
        
    
    
    