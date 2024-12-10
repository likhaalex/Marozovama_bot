import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

user_state = {}

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Что могу сделать для тебя?\n\n"
                         
                         "/help - Список доступных команд и фраз\n")

@dp.message(Command('help'))
async def send_help(message: types.Message):
    await message.answer("Вот что я могу: \n\n"
                         "/help - Список команд\n"
                         "Привет - Поздороваюсь"
                         "Как дела? - Расскажу как у меня дела\n"
                         "Пока - Попрощаюсь\n\n"
                         "Напиши любую из этих фраз, и я отреагирую!")
    
@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()

    if text == 'привет':
        await message.answer("Привет!")
    elif text == 'как дела?':
        await message.answer("У меня всё хорошо!")
    elif text == 'пока':
        await message.answer("Пока")

# Запуск бота
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())