import logging
from telegram import Update
import telegram.ext 

# Установите уровень логирования (необязательно)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Состояния для конечного автомата бота
START, NAME, AGE, COLLEGE, DONE = range(5)

# Словарь для хранения данных о пользователях
user_data = {}

# Функция начала работы с ботом
def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Привет! Я бот для сбора данных для справок. Напиши свое имя:")
    return NAME

# Функция для сбора имени пользователя
def get_name(update: Update, context: CallbackContext) -> int:
    user_data['name'] = update.message.text
    update.message.reply_text(f"Отлично, {user_data['name']}! Теперь укажи свой возраст:")
    return AGE

# Функция для сбора возраста пользователя
def get_age(update: Update, context: CallbackContext) -> int:
    user_data['age'] = update.message.text
    update.message.reply_text("Хорошо, последний шаг. Укажи свой учебный институт или колледж:")
    return COLLEGE

# Функция для сбора информации о месте учебы и записи данных в файл
def get_college(update: Update, context: CallbackContext) -> int:
    user_data['college'] = update.message.text
    with open('data.txt', 'a') as file:
        file.write(f"Имя: {user_data['name']}, Возраст: {user_data['age']}, Место учебы: {user_data['college']}\n")
    update.message.reply_text("Спасибо! Данные записаны. /start для начала сбора новых данных.")
    return ConversationHandler.END

# Функция для завершения общения с ботом
def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Операция отменена. /start для начала сбора данных снова.")
    return ConversationHandler.END

def main():
    # Инициализация бота
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Создание конечного автомата
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            AGE: [MessageHandler(Filters.text & ~Filters.command, get_age)],
            COLLEGE: [MessageHandler(Filters.text & ~Filters.command, get_college)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()
