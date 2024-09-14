from aiogram.dispatcher.filters.state import State, StatesGroup

class AdminStates(StatesGroup):
    waiting_for_answer = State()
    waiting_for_new_answer = State()
    waiting_for_new_answer_and_end = State()
    
    
class BroadcastState(StatesGroup):
    text = State()
    photo = State()
    button_name = State()
    button_url = State()
    preview = State()