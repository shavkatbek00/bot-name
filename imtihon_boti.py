from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import re

pattern = ("^\+?998?[0-9]{9}$")

bot = Bot("6272776673:AAGMrx1rBOo-sz14-P_ky4oldNgIDfJUiG4")
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage)

rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton("/create"))

class Form(StatesGroup):
    name = State()
    phone_number = State()
    email = State()

async def on_startup(_):
    print("bot t`g`ri ishladi")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=f"Assalomu aleykom {message.from_user.first_name} \n dd bb botimizga hush kelibsiz royhatdan otish uchun /create sozini bosing",
                         reply_markup=rkb)


@dp.message_handler(Text(equals="/create"))
async def fill_form(message: types.Message):
    await Form.name.set()
    await message.answer("Ism fmiliyangizni kiriting: ")
@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    """
    Set user name
    """
    async with state.proxy() as data:
        data['name'] = message.text


    await Form.next()
    await message.answer("Telefon raqamingizni kiriting: +998999999999")



@dp.message_handler(lambda message: re.fullmatch(pattern, message.text), state=Form.phone_number)
async def procces_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await Form.email.set()
    await message.answer("emailingizni kiriting: aaa@gmail.com")
@dp.message_handler(state=Form.email)
async def set_kasb(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await state.reset_state(with_data=False)

    data = await state.get_data()
    await message.answer(text=f"Ism: {data.get('name')},"
                                f"\n telefon nomer: {data.get('phone_number')}"
                                f"\n email adres: {data.get('email')}"
                         )
    await state.reset_state(with_data=True)



if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)





















# import re
#
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher.filters import Text
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.dispatcher import FSMContext
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
#
# # from aiogram.types import ParseMode
# # import aiogram.utils.markdown as md
#
# #           +998 93 999 99 99
# pattern = re.compile("^\+?[998]?[0-9]{9}$")
#
# bot = Bot('6272776673:AAGMrx1rBOo-sz14-P_ky4oldNgIDfJUiG4')
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
#
# rkb = ReplyKeyboardMarkup(resize_keyboard=True)
# rkb.add(KeyboardButton('/create'))
#
#
# class Form(StatesGroup):
#     name = State()
#     phone_number = State()
#     email = State()
#
#
# async def on_startub(_):
#     print("bot run succesfully")
#
#
# @dp.message_handler(commands=["start"])
# async def start_command(massage: types.Message):
#     await massage.answer(text=f"Assalomu alaykum {massage.from_user.first_name} botimizga xush kelibsiz",
#                          reply_markup=rkb)
#
#
# @dp.message_handler(commands="create")
# async def fil_form(message: types.Message):
#     await Form.name.set()
#     await message.answer("Ismingizni kiriting")
#
#
# @dp.message_handler(state=Form.name)
# async def set_name(message: types.Message, state: FSMContext):
#     """
#     Set user name
#     """
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await Form.next()
#     await message.answer("telefon nomeringizni kiriting")
#
#
#
#
#
#
#
# @dp.message_handler(lambda message: re.match(pattern, message.text), state=Form.phone_number)
# async def process_phone_number(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['email'] = message.text
#
# @dp.message_handler(lambda message: not message.text.isdigit(), state=Form.phone_number)
# async def avoid_age_format(message: types.Message):
#     await message.answer("nomer faqat sonlardan iborat bo`lsin")
#
# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.phone_number)
# async def protses_age_format(message: types.Message, state: FSMContext):
#      async with state.proxy() as data:
#           data["phone_number"] = int(message.text)
#      await Form.next()
#      await message.answer("email:")
#
# @dp.message_handler(state=Form.email)
# async def set_email(message: types.Message, state: FSMContext):
#      email = message.text
#      await state.update_data(email=email)
#      await state.reset_state(with_data=False)
#
#      data = await state.get_data()
#
#
#
#
#      msg = f"name: {data['name']}, \n phone: {data['phone_number']}, \n email: {data['email']}"
#      await bot.send_message(chat_id=message.from_user.id, text=msg)
#      await state.finish()
#
#
#
#
#
#
#
# @dp.message_handler(commands=["help"])
# async def start_command(massage: types.Message):
#     await massage.reply(text="o harfini tepasiga ' qo'yish kerak")
#

# if __name__ == '__main__':
#     executor.start_polling(dispatcher=dp,
#                            on_startup=on_startub,
#                            skip_updates=True)
