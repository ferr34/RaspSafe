from Crypto.Hash import SHA256
from bin import access as acc
import remote_control_bot as rcb 
import os 

def first_time():
    # First we need to choose a key to access the key, than we will check with a digest
    username = input("Please insert a username: ")
    key = input("Please choose a password:")
    
    print('Now you will insert encryption parameters. Please do not forget because you cannot recover them.')
    aes_parameters = []

    aes_parameters[0] = input("Insert AES key: ")
    aes_parameters[1] = input("Insert AES initialization vector: ")
    
    # Creating hidden folder
    folder_name = "data_to_protect_" + username
    print(folder_name) # test
    
    os.mkdir(folder_name)

    # Creating the hash for the password 
    hash_one = SHA256.new()
    password_param = username + "_" + key
    hash_one.update(password_param.encoding('utf-8'))
    update_file = open("utilities/hashes.txt","a")

    # Adding the hash to the file
    update_file.write(str(hash_one.digest()))
    update_file.close()

   # Hash for AES parameters
    aes_user_param = username + "_" + aes_parameters[0] + "_" + aes_parameters[1]

    update_aes_param = open("../utilities/recover_keys.txt","a")
    
    hash_two = SHA256.new()
    hash_two.update(aes_user_param.encoding('utf_8'))

    update_aes_param.write(str(hash_two.digest()))
    update_aes_param.close()
    

    print('Opening the safe...')
    
    # Accessing the safe
    acc.access_safe_menu(key)
    
    
    
    
    
    
    