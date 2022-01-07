# Bot to send information and remote controlling the safe 

import os 
import telepot # works on terminal

from telepot.loop import MessageLoop



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s:', command)

    if command == "/start": 
        bot.sendMessage('')


bot = telepot.Bot('5026547082:AAGgzOX1CrIfqCkrLbJdIHZqvcLY2m31n6k')
bot.loop(handle)