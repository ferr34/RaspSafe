# Script for creating logs - I'll store them in a file 

def add_log(log_timestamp):
    update_file = open("utilities/logs.txt","a")
    msg  = "Login attempt at " + log_timestamp

    update_file.write(msg)
    update_file.close()

def show_logs(): 
    with open("utilities/logs.txt") as f:
        for line in f:
            print(line)
    
    # Empty the file 
    make_file_empty = open("utilities/logs.txt","w").close()

