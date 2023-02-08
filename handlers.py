from TelegramBot.create import dp
from aiogram import types
from aiogram.dispatcher.filters import Filter
import random



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}, мы будем играть с тобой в конфетки')


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Пока я ещё ничего не умею, но обязательно научёсь')


@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Максимальное кол-во установлено {total}')



@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit():
        total -= int(message.text)
        await message.reply(f'На столе осталось {total} конфет')



