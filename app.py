import telebot
from config import TOKEN, keys
from classes import Converter, ConvException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_hl2_message(message):
    bot.send_message(message.chat.id, f"Для начала работы введите через пробел \
название исходной валюты, в какую валюту хотите перевести, \
а также количество денег. \
Пример: доллар рубль 120 (120 долларов хотите перевести в рубли). \
Доступные валюты можно посмотреть, введя /values")

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступны следующие валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types='text')
def convertation(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvException("Введите 3 значения")
        iz, to, amount = values
        itog = Converter.convert(iz, to, amount)
    except ConvException as e:
        bot.reply_to(message, e)
    except Exception as e:
        bot.reply_to(message, f"Не смог обработать команду:\n{e}")
    else:
        text = f'Цена {amount} {iz[:3]}. = {itog} {to[:3]}.'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
