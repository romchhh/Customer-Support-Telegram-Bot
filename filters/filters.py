from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from data.config import administrators, managers


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in administrators


class IsManager(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in managers