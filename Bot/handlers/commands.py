import telebot

import config

bot = config.settings.get_bot()


def _start(message: telebot.types.Message):
    from ..assets.reply_keyboards import hello_button as hello
    
    user = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.add(hello)
    reply_text = config.settings.get_messages()['send_hello']
        
    bot.send_message(
        chat_id=user,
        text=reply_text,
        reply_markup=keyboard
    )

def registration():
    bot.register_message_handler(
        callback=_start,
        commands=['start']
    )
    return
