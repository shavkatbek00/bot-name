import wikipedia
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import wikipedia

wikipedia.set_lang("uz")

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("❤", callback_data="like")],
    [InlineKeyboardButton("😜", callback_data="dislike")]
])

TOKEN = "5993718094:AAFuH_ciUd-v1c4TtA2hF5wZHFSjRFIgXJk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)


rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton(text="/help"))
rkb.add(KeyboardButton(text="/start"))

#
# @dp.message_handler(commands=["start"])
# async def start_command(massage: types.Message):
#     await massage.reply(text="Assalomu alaykum")
#
#
# @dp.message_handler(commands=["help"])
# async def start_command(massage: types.Message):
#     await massage.reply(text="o harfini tepasiga ' qo'yish kerak")


# @dp.message_handler()
# async def echo_ansver(massage: types.Message):
#     await massage.answer(text=massage.text.upper())


# @dp.message_handler(Text(equals="commandsss"))
# async def get_commma(massge: types.Message):
#     text = """
#     /help = yordam
#     /start = qayta boshlash
#     """
#
#     await massge.answer(text=text)


# @dp.message_handler(Text(equals=["salom"]))
# async def start_command(massage: types.Message):
#     await massage.reply(text="o harfini tepasiga ' qo'yish kerak")


# @dp.message_handler(Text(equals="s"))
# async def START_commma(massge: types.Message):
#     await bot.send_photo(chat_id=massge.from_user.id,
#                          photo="https://yandex.ru/images/search?pos=5&from=tabbar&img_url=http%3A%2F%2Fmobimg.b-cdn.net%2Fv3%2Ffetch%2F1f%2F1f409cc95f7ee2b80b3c440a4df4c9e2.jpeg%3Fw%3D1470%26r%3D0.5625&text=mountain&rpt=simage&lr=10335",
#                          caption="bu rasm sizga yoqdimi",
#                          reply_markup=ikb)





# @dp.message_handler(Text(equals="s"))
# async def START_commma(massge: types.Message):
#     await bot.send_photo(chat_id=massge.from_user.id,
#                          photo="https://yandex.ru/images/search?pos=5&from=tabbar&img_url=http%3A%2F%2Fmobimg.b-cdn.net%2Fv3%2Ffetch%2F1f%2F1f409cc95f7ee2b80b3c440a4df4c9e2.jpeg%3Fw%3D1470%26r%3D0.5625&text=mountain&rpt=simage&lr=10335",
#                          caption="bu rasm sizga yoqdimi",
#                          reply_markup=rkb)
#


# # @dp.callback_query_handler(text="like")
# # async def calll(callback: types.CallbackQuery):
# #     await callback.answer("you like it")
# #
# # @dp.callback_query_handler(text="dislike")
# # async def calll(callback: types.CallbackQuery):
# #     await callback.answer("you dislake it")
#
#
# @dp.callback_query_handler()
# async def calll(callback: types.CallbackQuery):
#     if callback.data == 'like':
#         await callback.answer("you like it")
#     elif callback.data == "dislike":
#         await callback.answer("you dislike it")


@dp.message_handler()
async def sendw(massage: types.Message):
    try:
        qaytgan = wikipedia.summary(massage.text)
        await massage.answer(qaytgan)
    except:
        await massage.answer("bu mavzuga oid ma'lumot yo`q")


# @dp.message_handler(Text(equals=["manzil"]))
# async def slo(massage: types.Message):
#     await bot.send_location(chat_id=massage.from_user.id,
#                             latitude=41.287629, longitude=69.219397)










if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
