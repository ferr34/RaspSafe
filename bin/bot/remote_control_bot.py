# Bot to send information and remote controlling the safe 

import os 
import telepot 
import datetime
import time 
from telepot.loop import MessageLoop

bot = telepot.Bot('token')

def handle(msg,info):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s:', command)

    if command == "/start": 
        bot.sendMessage(chat_id, 'Welcome to the Remote Control Bot for RaspSafe - A safe for your RaspBerry')
        bot.sendMessage(chat_id, 'Now the safe is linked with this Bot, thus you can directly control it from here.')
        bot.sendMessage(chat_id, 'Can I help you futhermore? [y/N]')

        if msg == 'y': 
            list_options()
        else:
            bot.sendMessage(chat_id, 'Ok! You can now go back to the safe. Bye!'); 
    
    # Listing other commands...
    if command == "/report":
        bot.sendMessage(chat_id, 'Access Safe attempt. Info: %s', info)

    if command == "/enc_done":
        bot.sendMessage(chat_id, "Safe has now been encrypted. Encryption concluded on %s", info)



def list_options(): 
    print('Options available: ')

def send_alert(info):
    handle("/report",info)

def send_message_enc(info):
    handle("/enc_done",info)

def call_bot():
    MessageLoop(bot, handle).run_as_thread()









