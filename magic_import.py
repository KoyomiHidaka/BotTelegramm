import logging
from random import randint
from aiogram import Bot, Dispatcher
from aiogram import types

bot = Bot(token="5514168500:AAE6YTfVmD_YyW3h28eQCz24NY9vr-HgkFo", parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)



