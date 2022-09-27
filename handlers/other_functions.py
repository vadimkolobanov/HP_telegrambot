from aiogram import types, Dispatcher

from bot_configure import bot
from bot_configure import config
from keyboards.vk_parser_keyboard import kb_client


async def other_text(message: types.Message):
    await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'other_messages'), reply_markup=kb_client)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(other_text)