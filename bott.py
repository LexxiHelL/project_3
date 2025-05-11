# Импортируем необходимые классы.
import logging

from scrypt import *
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from datetime import datetime

BOT_TOKEN = '7639903209:AAFlVuMrFZwLkVZ6QCXgkpRWXcGuWLjWbcY'
# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


var = [['/number'], ['/name'], ['/email'], ['/VK'], ['/date'], ['/time']]
var_markup = ReplyKeyboardMarkup(var, one_time_keyboard=False)

# флаг для работы реализатора handle
NUM, FIO, EMAIL, VK = False, False, False, False


# Определяем функцию-обработчик сообщений.
# У неё два параметра, updater, принявший сообщение и контекст - дополнительная информация о сообщении.
async def start(update, context):
    await update.message.reply_text(f'Здравствуй, {update.message.from_user.first_name}!\n'
                                    f'Пришли мне: или номер телефона, или ФИО, или почту, или VK'
                                    f' - и я найду этого человека!\n'
                                    f'Также я могу прислать сегодняшнюю дату и время!', reply_markup=var_markup)


# время
async def get_time(update, context):
    await update.message.reply_text(f" текущее время: {datetime.now().strftime('%H:%M:%S')}")


# дата
async def get_date(update, context):
    await update.message.reply_text(f" текущая дата: {datetime.now().strftime('%d.%m.%y')}")


# Фио
async def ask_name(update, context):
    """Запрашивает ФИО"""
    await update.message.reply_text(
        "Отправьте мне ФИО")
    global FIO
    FIO = True


# майл
async def ask_email(update, context):
    """Запрашивает email"""
    await update.message.reply_text(
        "Отправьте мне Email")
    global EMAIL
    EMAIL = True


# ВК
async def ask_VK(update, context):
    """Запрашивает VK"""
    await update.message.reply_text(
        "Отправьте мне VK id")
    global VK
    VK = True


# номер телефона
async def ask_phone(update, context):
    """Запрашивает номер телефона"""
    await update.message.reply_text(
        "Отправьте мне номер телефона в любом формате:\n"
        "Примеры: 79161234567, 89651234567"
    )
    global NUM
    NUM = True


# обработчик всех поступающих данных
async def handle(update, context):
    """Обрабатывает номер, присланный текстом"""
    text = update.message.text

    global NUM, FIO, EMAIL, VK

    if NUM:
        if len(text) == 11:  #
            formatted_phone = f"{text}"

            await update.message.reply_text(
                f"Номер телефона:  {'+' + formatted_phone}"
            )
            NUM = False
            user = update.message.from_user
            cur.execute(f'''SELECT 1 FROM Numbers_of_hum WHERE num = {formatted_phone}''')
            exists = cur.fetchone()

            if not exists:
                add_user_data(formatted_phone)
            a = num_script(formatted_phone)
            for i in range(12):
                await update.message.reply_text(f"{a[i]}")

    if FIO:
        await update.message.reply_text(f'Введенное имя: {text}')
        FIO = False
        a = name_script(text)
        for i in range(12):
            await update.message.reply_text(f"{a[i]}")
    if EMAIL:
        await update.message.reply_text(f'Введенное email: {text}')
        EMAIL = False
        a = email_script(text)
        for i in range(12):
            await update.message.reply_text(f"{a[i]}")
    if VK:
        await update.message.reply_text(f'Введенный аккаунт: {text}')
        VK = False
        a = VK_script(text)
        for i in range(12):
            await update.message.reply_text(f"{a[i]}")


# реализатор, главная функция
def main():
    # Создаём объект Application.
    app = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем обработчик в приложении.
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("number", ask_phone))
    app.add_handler(CommandHandler("email", ask_email))
    app.add_handler(CommandHandler("VK", ask_VK))
    app.add_handler(CommandHandler("name", ask_name))
    app.add_handler(CommandHandler("date", get_date))
    app.add_handler(CommandHandler("time", get_time))

    # Запускаем приложение.
    app.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
