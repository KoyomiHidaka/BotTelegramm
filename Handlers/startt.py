import re
import time

from aiogram import types, Dispatcher, Bot

from magic_import import randint, bot


# @dp.message_handler(commands=["Start"])
async def startcmd(message: types.Message):
    # k = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    # b = ["/choose_language", "/special_buttons", "/info", "/random", "Закрыть меню"]
    # k.add(*b)
    await message.answer("Напиши: /help")


# @dp.message_handler(lambda message:  message.text == "Закрыть меню")
async def close(message: types.Message):
    await message.answer("Выполнено!", reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(commands="Тест1")
async def cmd_test1(message: types.Message):
    await message.answer("Test 1")


# Хэндлер на команду /test2 answer-просто ответ, а reply-ответ с ответом


# @dp.message_handler(commands="test2")
async def cmd_test2(message: types.Message):
    await message.answer("Test 2")


# @dp.message_handler(commands="help")
async def cmd_help(message: types.Message):
    await message.answer("Пока что есть такие функции(еще можно просто писать сообщения например Pythonf и Extra0(не "
                         "обязательно писать я это для себя написал)"
                         "список команд ниже(советую начать с команды '/Описание':")
    await message.answer("/Описание")
    await message.answer("/choose_language")
    await message.answer("/special_buttons")
    await message.answer("/info")
    await message.answer("/random")
    await message.answer("/Pythonf")
    await message.answer("/Extra0")


async def description(message: types.message):
    await message.answer("Этот бот умеет разные команды весь список ты найдешь если вызовешь команду /help, "
                         "а еще в ответ на любое сообщение не относящееся"
                         " к командам и особым сообщениям(Pythonf, Extra0) он "
                         "не будет отвечать тебе почти тем же сообщением так что не пиши что вздумается! ")


# @dp.message_handler(commands="choose_language")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Java", "Python", "Потом выберу"]
    keyboard.add(*buttons)
    await message.answer("Что выберешь?", reply_markup=keyboard)


async def dictionary(message: types.message):
    ke = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Yes"]
    ke.add(*buttons)
    await message.answer("Начинаем?", reply_markup=ke)


async def fill(message: types.message):
    await message.answer("Начинаю подготовку! а вы пока придумаете имя словаря и вызовите /name и имя словаря",
                         reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Введи первый Ключ в виде Key и слово которое"
                         " будет воспринято как значение ключа для значений используйте Value")



async def key_and_values_and_assembly_and_other_cool_functions(message: types.message) -> object:
    global key_approved_final, value_approved_final, name_approved, \
        value_approved, namedict, newkey_approved, newvalue_approved



    if "Name" in message.text:
        name_filter = ["Name"]
        name_dirt = message.text
        new_name_str = name_dirt.split()
        name_clean = [word for word in new_name_str if word not in name_filter]
        name_approved = ' '.join(name_clean)  # is Dictionary Name

        await message.answer(f"Имя словаря - {name_approved}")
        return name_approved



    if "Key" in message.text:
        key_filter = ["Key"]
        key_dirt = message.text
        new_str = key_dirt.split()
        key_clean = [word for word in new_str if word not in key_filter]
        key_approved = ' '.join(key_clean)  # is Key
        key_approved_final = key_approved
        await message.answer(f"Your Key is {key_approved_final}")
        return key_approved_final



    if "Value" in message.text:
        value_filter = ["Value"]
        value_dirt = message.text
        new_value_str = value_dirt.split()
        value_clean = [word for word in new_value_str if word not in value_filter]
        value_approved = ' '.join(value_clean)  # is Value
        value_approved_final = value_approved
        await message.answer(f"Your Value is {value_approved_final}")
        return value_approved_final



    if "/assembly" in message.text:
        await message.answer(
            f"Your name of Dictionary is {name_approved} Your Key is {key_approved_final} and You Value is "
            f"{value_approved_final} If you want to extend Your Dictionary type /add command")
        namedict = name_approved
        namedict = {key_approved_final: value_approved_final}
        print(namedict)

    if "/show" in message.text:
        await message.answer(f"Your Dictionary  {name_approved}={namedict}")
        time.sleep(2)
        await message.answer(f"Сейчас будет выведен код для копирования :)")
        await message.answer(f"{name_approved}={namedict}")



#  @dp.message_handler(lambda message: message.text == "Java")


async def java(message: types.Message):
    await message.answer("В 2 раза больше удачи!", reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(lambda message: message.text == "Python")
async def python(message: types.Message):
    await message.answer("Удачи!", reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(lambda message: message.text == "Потом выберу")
async def potom(message: types.Message):
    await message.answer("Не забудь!", reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(commands="special_buttons")
async def cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Запросить геолокацию", request_location=True))
    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
    keyboard.add(types.KeyboardButton(text="Создать викторину",
                                      request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    keyboard.add(types.KeyboardButton(text="Закрыть меню"))
    await message.answer("Выберите действие:", reply_markup=keyboard)


# @dp.message_handler(lambda message: message.text == "Закрыть меню")
async def close_menu(message: types.Message):
    await message.answer("Готово!", reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(commands="info")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Создатель", url="https://steamcommunity.com/id/dontfollow")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Информация:", reply_markup=keyboard)


async def kivy(message: types.Message):
    k = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b = ["About Kivy", "Source code"]
    k.add(*b)
    k.add(types.KeyboardButton(text="Close", callback_data="Close"))
    await message.answer("Выбери действие", reply_markup=k)


async def about_kivy(message: types.message):
    await message.answer("Kivy это то с помощью чего ты сможешь писать сложные интерфейсы")
    await message.answer("2 основных импорта это")
    await message.answer(f"from kivy.app import App")
    await message.answer(f"from kivy.uix.button import Button")


async def source_code(message: types.Message):
    photo = open("Screenshot_19.png", "rb")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


async def closekivyfunc(message: types.message):
    await message.answer("https://open.spotify.com/track/7kEva2rxsNMn07fyfZMRRn?si=e3a7e745f05847e9",
                         reply_markup=types.ReplyKeyboardRemove())


async def screenshots_from_d_desktopp(message: types.message):
    k = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b = ["Deploy", "Close"]
    k.add(*b)
    await message.answer("Выбери действие", reply_markup=k)


async def deploy(message: types.message):
    await message.answer("Deploying in progress /......")
    photo1 = open("Screenshot_1.png", "rb")
    photo2 = open("Screenshot_2.png", "rb")
    photo3 = open("Screenshot_3.png", "rb")
    photo4 = open("Screenshot_4.png", "rb")
    photo5 = open("Screenshot_5.png", "rb")
    photo6 = open("Screenshot_6.png", "rb")
    photo7 = open("Screenshot_7.png", "rb")
    photo8 = open("Screenshot_8.png", "rb")
    photo9 = open("Screenshot_9.png", "rb")
    photo10 = open("Screenshot_10.png", "rb")
    photo11 = open("Screenshot_11.png", "rb")
    photo12 = open("Screenshot_12.png", "rb")
    photo13 = open("Screenshot_13.png", "rb")
    photo14 = open("Screenshot_14.png", "rb")
    photo15 = open("Screenshot_15.png", "rb")
    photo16 = open("Screenshot_16.png", "rb")
    photo17 = open("Screenshot_17.png", "rb")
    photo18 = open("Screenshot_18.png", "rb")


    await bot.send_photo(chat_id=message.chat.id, photo=photo1)
    await bot.send_photo(chat_id=message.chat.id, photo=photo2)
    await bot.send_photo(chat_id=message.chat.id, photo=photo3)
    await bot.send_photo(chat_id=message.chat.id, photo=photo4)
    await bot.send_photo(chat_id=message.chat.id, photo=photo5)
    await bot.send_photo(chat_id=message.chat.id, photo=photo6)
    await bot.send_photo(chat_id=message.chat.id, photo=photo7)
    await bot.send_photo(chat_id=message.chat.id, photo=photo8)
    await bot.send_photo(chat_id=message.chat.id, photo=photo9)
    await bot.send_photo(chat_id=message.chat.id, photo=photo10)
    await bot.send_photo(chat_id=message.chat.id, photo=photo11)
    await bot.send_photo(chat_id=message.chat.id, photo=photo12)
    await bot.send_photo(chat_id=message.chat.id, photo=photo13)
    await bot.send_photo(chat_id=message.chat.id, photo=photo14)
    await bot.send_photo(chat_id=message.chat.id, photo=photo15)
    await bot.send_photo(chat_id=message.chat.id, photo=photo16)
    await bot.send_photo(chat_id=message.chat.id, photo=photo17)
    await bot.send_photo(chat_id=message.chat.id, photo=photo18)


async def close_deploy(message: types.message):
    await message.answer(" ", reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


# @dp.callback_query_handler(text="random_value")
# async def send_random_value(call: types.CallbackQuery):
#    await call.message.answer(str(randint(1, 10)))
#    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=False)
    # или просто await call.answer()


async def help_text_message(message: types.message):
    await message.answer("F строки это строки в которые можно встраивать переменные как в java script пример ниже")
    await message.answer('f"text and {переменная}"')


async def extra0(message: types.message):
    await message.answer("Экстра информация: для того чтобы зарегистрировать Хэндлер на определенный"
                         " текст можно просто вписать слово text = 'тут текст' пример ниже")
    await message.answer('dp.register_message_handler(help_text_message, text="Pythonf")')


async def stage1(message: types.message):
    if "stage1" in message.text:
        await message.answer(f"Stage1 has been started!!!")



async def random(message: types.message):
    await message.answer("Type first number")
    firstnum = message.text
    await message.answer("Type second number")
    secondnum = message.text
    await message.answer(f"Your number first is {firstnum} and second is {secondnum}")
    await message.answer(str(randint(firstnum, secondnum)))


async def time1(message: types.message):
    await message.answer("Time")
    k = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b = ["1m", "5m"]
    k.add(*b)
    await message.answer("How much?", reply_markup=k)


async def minute1(message: types.message):
    await message.answer("Minute1 - type text", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"1 minute")
    time.sleep(60)
    await message.answer(f"5Sec")









def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(startcmd, commands="Start")
    dp.register_message_handler(time1, commands="time")
    dp.register_message_handler(minute1, text="1m")
    dp.register_message_handler(close, text="Закрыть меню")
    dp.register_message_handler(cmd_test1, commands="Тест1")
    dp.register_message_handler(cmd_test2, commands="test2")
    dp.register_message_handler(cmd_help, commands="help")
    dp.register_message_handler(cmd_start, commands="choose_language")
    dp.register_message_handler(dictionary, text="dictionary")
    dp.register_message_handler(fill, text="Yes")
    dp.register_message_handler(java, text="Java")
    dp.register_message_handler(python, text="Python")
    dp.register_message_handler(potom, text="Потом выберу")
    dp.register_message_handler(cmd_special_buttons, commands="special_buttons")
    dp.register_message_handler(close_menu, text="Закрыть меню")
    dp.register_message_handler(cmd_inline_url, commands="info")
    dp.register_message_handler(cmd_random, commands="random")
    dp.register_message_handler(extra0, commands="Extra0")
    dp.register_message_handler(kivy, commands="kivy")
    dp.register_message_handler(closekivyfunc, text="Close")
    dp.register_message_handler(about_kivy, text="About Kivy")
    dp.register_message_handler(source_code, text="Source code")
    dp.register_message_handler(help_text_message, commands="Pythonf")
    dp.register_message_handler(description, commands="Описание")
    dp.register_message_handler(screenshots_from_d_desktopp, text="Screenshot")
    dp.register_message_handler(deploy, text="Deploy")
    dp.register_message_handler(close_deploy, text="Close")
    dp.register_message_handler(random, text="Random")
    dp.register_message_handler(key_and_values_and_assembly_and_other_cool_functions)

    # dp.register_message_handler(any_text_message)
