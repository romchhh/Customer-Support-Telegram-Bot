from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


def get_start_dialog_keyboard(question_id):
    keyboard = InlineKeyboardMarkup()
    start_dialog_button = InlineKeyboardButton(text="Почати діалог", callback_data=f"start_dialog:{question_id}")
    keyboard.add(start_dialog_button)
    return keyboard

def get_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = KeyboardButton(text="Завершити діалог")
    keyboard.add(cancel_button)
    return keyboard

def get_manager_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Мої активні діалоги✅", callback_data="active_dialogs"),
        InlineKeyboardButton(text="Мої завершені діалоги❌", callback_data="completed_dialogs"),
    ]
    keyboard.add(*buttons)
    return keyboard


def get_admin_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Активні діалоги✅", callback_data="adminactive_dialogs"),
        InlineKeyboardButton(text="Завершені діалоги❌", callback_data="admincompleted_dialogs"),
        InlineKeyboardButton(text="Статистика", callback_data='user_statistic'),
        InlineKeyboardButton(text="Розсилка", callback_data='mailing')
    ]
    keyboard.add(*buttons)
    return keyboard


def get_preview_markup():
    markup = InlineKeyboardMarkup()
    preview_button = InlineKeyboardButton("📤 Отправить", callback_data="send_broadcast")
    cancel_button = InlineKeyboardButton("❌ Отменить", callback_data="cancel_broadcast")
    markup.row(preview_button, cancel_button)
    markup.one_time_keyboard = True
    return markup

def get_back_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    back_button = InlineKeyboardButton("Назад", callback_data="adminback")
    keyboard.add(back_button)
    return keyboard