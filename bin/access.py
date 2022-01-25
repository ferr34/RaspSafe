from Crypto.Hash import SHA256
import os
import sys
import datetime 
import time
from bin.menus import menu as mn 
from bot import remote_control_bot as rmc
import encrypt as enc

def access_safe_menu(password):
    if password != "":
        # Password already read or first time, password chosen
        print('Password already read...')

        # Jumping to the menu 

    else:
        try_counter = 0
        while try_counter < 2:
            access_key = input('Insert the password: ')
    
            hash_one = SHA256.new()
            hash_one.update(access_key.encoding('utf-8'))
            update_file = open("utilities/hashes.txt","r").read()
        
            if update_file == hash_one:
                # Users validated
                print('User authenticated. Welcome back.')
                
                # Opening the menu 
                mn.show_menu()

            else:
                # Sending telegram message
                # first time method
                print('Password not valid. Retry please.')
                today = datetime.date.today()
                rmc.send_alert(str(today.ctime()))

                try_counter = try_counter + 1
                
        if try_counter >= 3:
            # Safe needs to be ciphered 

            print('Too many attempts. The data will be now ciphered.')       
            enc.cipher_data()

            today = datetime.date.today()
            # Sending message with the bot 
            rmc.send_message_enc(str(today.ctime()))

         
        
    
    
    