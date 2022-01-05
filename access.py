from Crypto.Hash import SHA256
import os
import sys


def access_safe_menu(password):
    
    if password != "":
        # Password already read or first time, password chosen
        print('Password already read...')
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
            else:
                # Sending telegram message ->  Setting up the bot in
                # first time method
                print('Password not valid. Retry please.')
                try_counter = try_counter + 1
                
                
         
        
    
    
    