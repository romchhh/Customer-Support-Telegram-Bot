from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  
    support_button = KeyboardButton(text="Зв'язатися з нами👨🏼‍💻")
    keyboard.add(support_button)
    return keyboard


def get_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = KeyboardButton(text="Відміна")
    keyboard.add(cancel_button)
    return keyboard
