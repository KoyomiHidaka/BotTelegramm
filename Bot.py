

from aiogram import executor

from magic_import import dp


async def start(_):
    print("Starting Bot /..... Done!")



from Handlers import startt

startt.reg_handlers(dp)


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=start)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=start)




#  We can use simple html tags for our messages. Message with html tag very beautiful


# @dp.message_handler(commands="test1") Реагирует на команду test1 вместо test1 можно написать что угодно
# async def cmd_test1(message: types.Message): Просто надо
# await message.answer("Test 1")
# await message.answer("Сообщение с <u>HTML-разметкой</u>")
# await message.answer("Сообщение без <s>какой-либо разметки</s>", parse_mode="") Ответ на сообщение test1

# @dp.message_handler(commands="test1")
# async def cmd_test1(message: types.Message):
#    await message.answer("Test 1") структура реагирования на команды вместо answer можно написать reply

# /-----------------------------------------------------------------------------------------------------------------/
# Ответы на сообщения
# @dp.message_handler()
# async def any_text_message(message: types.Message):
#    await message.answer(message.text)

# /---------------------------------------------------Кнопки-------------------------------------------------------------------/
# @dp.message_handler(commands="start")
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) Чтобы не были слишком большими
#     buttons = ["Java", "Python"] Имя кнопок
#     keyboard.add(*buttons) Добавит кнопки
#     await message.answer("Что выберешь?", reply_markup=keyboard)
# /------------------------------------Реакция на кнопки--------------------------------------------/
# @dp.message_handler(lambda message: message.text == "Java") lambda сообщение: /
# /если текст сообщения(message.text) равен(==) /
# /Java то ответить await message.reply("В 2 раза больше удачи!")
# async def Java(message: types.Message): просто функция
#    await message.reply("В 2 раза больше удачи!") ответ на кнопку

# /--------------------------Особые кнопки----------------------------------------------------------/

# @dp.message_handler(commands="special_buttons")
# async def cmd_special_buttons(message: types.Message):
#    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    keyboard.add(types.KeyboardButton(text="Запросить геолокацию", request_location=True))
#    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
#    keyboard.add(types.KeyboardButton(text="Создать викторину",
#                                      request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
#    keyboard.add(types.KeyboardButton(text="Закрыть меню"))
#    await message.answer("Выберите действие:", reply_markup=keyboard)
# @dp.message_handler(lambda message: message.text == "Закрыть меню")
# async def close_menu(message: types.Message):
#    await message.answer("Готово!", reply_markup=types.ReplyKeyboardRemove())

# /--------------------------------------Инлайн кнопки(под сообщениями)----------------------------------------/

# @dp.message_handler(commands="inline_url")
# async def cmd_inline_url(message: types.Message):
#    buttons = [
#        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
#        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
#    ]
#    keyboard = types.InlineKeyboardMarkup(row_width=1)
#    keyboard.add(*buttons)
#    await message.answer("Кнопки-ссылки", reply_markup=keyboard)
