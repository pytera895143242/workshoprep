from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
from .callbak_data import st
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

content_chat = -1001631961913
ids_user = []

markup_fell = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Четко 😎', callback_data='crazy')
bat_b = types.InlineKeyboardButton(text='Хренова', callback_data='bad')
bat_c = types.InlineKeyboardButton(text='Пойдёт', callback_data='good')

markup_fell.add(bat_a)
markup_fell.add(bat_b)
markup_fell.add(bat_c)

country = 'kz' #kz / kr / uzb

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    reg_user(message.chat.id, message.text[7:])
    if message.text[7:] == 'kz':
        await bot.copy_message(chat_id=message.chat.id,from_chat_id=content_chat,message_id=8)
        await asyncio.sleep(2)
        await message.answer("""Вахххх кто пришёл)) Қалайсын?
Как настрой?)""",reply_markup=markup_fell)


    if message.text[7:] == 'uzb':
        await bot.copy_message(chat_id=message.chat.id, from_chat_id=content_chat, message_id=284)
        await asyncio.sleep(2)
        await message.answer("""Вахххх кто пришёл)) Калей сан?
Как настрой?)""", reply_markup=markup_fell)


    if message.text[7:] == 'kr':
        await bot.copy_message(chat_id=message.chat.id, from_chat_id=content_chat, message_id=223)
        await asyncio.sleep(2)
        await message.answer("""Вахххх кто пришёл)) Канадайсын?
Как настрой?)""", reply_markup=markup_fell)

        bot.approve_chat_join_request()


