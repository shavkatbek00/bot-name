from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5534309705:AAFGgiCiXsG0N7ScgV9YSEnZzLCosIIKNcI"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)

@dp.message_handler(commands=["start"])
async def start_command(massage: types.Message):
    await massage.reply(text="qalaysan")


@dp.message_handler(commands=["help"])
async def start_command(massage: types.Message):
    await massage.reply(text="o harfini tepasiga ' qo'yish kerak")


# @dp.message_handler()
# async def echo_ansver(massage: types.Message):
#     await massage.answer(text=massage.text.upper())


@dp.message_handler(Text(equals="commandsss"))
async def get_commma(massge: types.Message):
    text = """
    /help = yordam
    /start = qayta boshlash
    """

    await massge.answer(text=text)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
