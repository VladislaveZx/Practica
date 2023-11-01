import config
import telebot

import handlers


def load_handlers(bot: telebot.TeleBot):
    handlers.commands.registration()
    handlers.messages.registration()
    handlers.callbacks.registration()


def main():
    load_handlers(bot=config.settings.get_bot())


if __name__ == '__main__':
    main()
