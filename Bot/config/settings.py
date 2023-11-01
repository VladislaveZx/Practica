import json
import telebot

def get_bot():
    file = open('Bot/config/keys.json')
    keys = json.load(file)
    token = keys['token']
    bot = telebot.TeleBot(token)
    
    return bot


def get_messages():
    from . import paths
    keys = json.loads(paths.keys_json)
    return keys
