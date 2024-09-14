from main import bot, dp, Dispatcher
from filters.filters import *
from aiogram import types

from keyboards.user_keyboards import get_start_keyboard, get_cancel_keyboard
from keyboards.admin_keyboards import get_start_dialog_keyboard
from database.user_db import *
from aiogram.dispatcher import FSMContext
from states.user_states import SupportStates
from callbacks.admin_callbacks import register_callbacks
from callbacks.user_callbacks import register_callbacks
from data.config import managers, administrators
from keyboards.admin_keyboards import get_manager_keyboard, get_admin_keyboard

html = 'HTML'

async def antiflood(*args, **kwargs):
    m = args[0]
    await m.answer("Не спеши :)")

async def on_startup(dp):
    # await scheduler_jobs()
    me = await bot.get_me()
    # await bot.send_message(logs, f"Бот @{me.username} запущений!")
    print(f"Бот @{me.username} запущений!")

async def on_shutdown(dp):
    me = await bot.get_me()
    # await bot.send_message(logs, f'Bot: @{me.username} зупинений!')
    print(f"Bot: @{me.username} зупинений!")

@dp.message_handler(IsPrivate(), commands=["start"])
@dp.throttled(antiflood, rate=1)
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user = message.from_user
    keyboard = get_start_keyboard()
    add_user(user_id, user_name)
    greeting_message = f"Привіт, {user.username}! \nЩоб зв'язатися з нашою підтримкою, натисніть кнопку знизу🤗."
    await message.answer(greeting_message, reply_markup=keyboard)
    

@dp.message_handler(text="Зв'язатися з нами👨🏼‍💻", state="*")
async def contact_support(message: types.Message, state: FSMContext):
    await message.answer("Будь ласка, напишіть ваше питання.", reply_markup=get_cancel_keyboard())
    await SupportStates.waiting_for_question.set()

@dp.message_handler(state=SupportStates.waiting_for_question)
async def receive_question(message: types.Message, state: FSMContext):
    keyboard = get_start_keyboard()
    if message.text.lower() == "відміна":
        await state.finish()
        await message.answer("Щоб зв'язатися з нашою підтримкою, натисніть кнопку знизу🤗.", reply_markup=keyboard)
        return

    user_question = message.text
    user_id = message.from_user.id
    user_name = message.from_user.username or message.from_user.full_name
    question_id = add_question_to_db(user_id, user_name, user_question)

    await message.answer("Дякуємо за ваше питання! Наші менеджери зв'яжуться з вами найближчим часом.", reply_markup=keyboard)

    for manager_id in managers:
        manager_message = (
            f"Питання від користувача @{user_name}:\n"
            f"\n<b>{user_question}</b>\n"
        )
        await bot.send_message(
            manager_id,
            manager_message,
            reply_markup=get_start_dialog_keyboard(question_id),
        )
    await SupportStates.waiting_for_new_question.set()
    await state.update_data(manager_id=None, question_id=question_id)

@dp.message_handler(IsPrivate(), commands=["manager"])
async def admin_start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user = message.from_user
    
    if user_id in managers:
        greeting_message = f"Привіт, {user.username}! \nВи є менеджером. Будь ласка, оберіть дію нижче:"
        await message.answer(greeting_message, reply_markup=get_manager_keyboard())
        
        
@dp.message_handler(IsPrivate(), commands=["admin"])
async def admin_start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user = message.from_user
    
    if user_id in administrators:
        greeting_message = f"Привіт, {user.username}! \nВи є адміністратором. Будь ласка, оберіть дію нижче:"
        await message.answer(greeting_message, reply_markup=get_admin_keyboard())
