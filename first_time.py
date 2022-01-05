from Crypto.Hash import SHA256
import access as acc

def first_time():
    # First we need to choose a key to access the key, than we will check with a digest
    
    key = input("Please choose a password:")
    
    # Creating the hash
    hash_one = SHA256.new()
    hash_one.update(key.encoding('utf-8'))
    update_file = open("utilities/hashes.txt","a")
    
    # Adding the hash to the file
    update_file.write(str(hash_one.digest()))
    update_file.close()
    
    # Link with the Telegram Bot -> Remote control for ciphering
    
    
    # Accessing the safe
    acc.access_safe_menu(key)
    
    
    
    
    
    
    