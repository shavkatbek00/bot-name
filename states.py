import re

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from konsfigu import TOKEN
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from aiogram.types import ParseMode
# import aiogram.utils.markdown as md

#           +998 93 999 99 99
pattern = re.compile("^\+?[998]?[0-9]{9}$")

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton('Ariza to`ldirish'))


class Form(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    email = State()


async def on_startub(_):
    print("bot run succesfully")


@dp.message_handler(commands=["start"])
async def start_command(massage: types.Message):
    await massage.answer(text="Assalomu alaykum botimizga xush kelibsiz",
                         reply_markup=rkb)


@dp.message_handler(Text(equals="Ariza to`ldirish"))
async def fil_form(message: types.Message):
    await Form.name.set()
    await message.answer("Ismingizni kiriting")


@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    """
    Set user name
    """
    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    await message.answer("yoshingizni kiriting")


@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def avoid_age_format(message: types.Message):
    await message.answer("Yosh faqat sonlardan iborat bo`lsin")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def protses_age_format(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = int(message.text)

    await Form.next()
    await message.answer("Telefon raqmni kiriting:")


@dp.message_handler(lambda message: re.match(pattern, message.text), state=Form.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    msg = f"name: {data['name']}, \n age: {data['age']}, \n phone: {data['phone_number']}"
    await bot.send_message(chat_id=message.from_user.id, text=msg)
    await state.finish()


@dp.message_handler(commands=["help"])
async def start_command(massage: types.Message):
    await massage.reply(text="o harfini tepasiga ' qo'yish kerak")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startub,
                           skip_updates=True)
