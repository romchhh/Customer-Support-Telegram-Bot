from aiogram.dispatcher.filters.state import State, StatesGroup


class SupportStates(StatesGroup):
    waiting_for_question = State()
    waiting_for_new_question = State()