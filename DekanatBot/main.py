import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from telegram import Update

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота, который вы получили от BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Состояния для конечного автомата
NAME, SURNAME, DONE = range(3)

# Словарь для хранения ФИО пользователя
user_data = {}

# Создаем директорию для хранения файлов, если она не существует
if not os.path.exists("user_data"):
    os.makedirs("user_data")

# Функция для начала ввода ФИО
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Давай начнем. Введи свое имя:")
    return NAME

# Функция для получения имени пользователя
def get_name(update: Update, context: CallbackContext):
    user_data['name'] = update.message.text
    update.message.reply_text(f"Отлично, {user_data['name']}! Теперь введи свою фамилию:")
    return SURNAME

# Функция для получения фамилии пользователя
def get_surname(update: Update, context: CallbackContext):
    user_data['surname'] = update.message.text
    full_name = f"{user_data['name']} {user_data['surname']}"
    user_id = update.message.from_user.id

    # Сохраняем ФИО пользователя в файл
    with open(f"user_data/{user_id}.txt", "w") as file:
        file.write(full_name)

    update.message.reply_text(f"Спасибо, {full_name}! Твое ФИО было сохранено.")
    return ConversationHandler.END

# Функция для отмены операции
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Операция отменена.")
    return ConversationHandler.END

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Создаем конечный автомат для ввода ФИО
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            SURNAME: [MessageHandler(Filters.text & ~Filters.command, get_surname)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()