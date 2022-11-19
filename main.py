import telebot as tg
import requests
import logging
import config

bot = tg.TeleBot(config.TOKEN)
user_id = 0


@bot.message_handler(commands=["auth"])
def auth(message):
    pass


@bot.message_handler(commands=["temp"])
def get_temp(message):
    try:
        temperature = get_single_value(config.SERVER_HOST, config.TEMP_ENDP)
        bot.send_message(message.chat.id, "Temperature is " + temperature)
    except IndexError:
        bot.send_message(message.chat.id, "No values, unfortunately :(")
    bot.message_handler()


@bot.message_handler(commands=['light'])
def get_light(message):
    try:
        light = get_single_value(config.SERVER_HOST, config.LIGHT_ENDP)
        bot.send_message(message.chat.id, "Light is " + light)
    except IndexError:
        bot.send_message(message.chat.id, "No values, unfortunately :(")
    bot.message_handler()


@bot.message_handler(commands=["pir"])
def get_pir(message):
    try:
        pir = get_single_value(config.SERVER_HOST, config.PIR_ENDP)
        bot.send_message(message.chat.id, "PIR is " + pir)
    except IndexError:
        bot.send_message(message.chat.id, "No values, unfortunately :(")
    bot.message_handler()


def get_single_value(host, endp):
    raw_data = requests.get(host + endp)
    values = raw_data.text.split(",")
    return values[1]


if __name__ == "__main__":
    logger = tg.logger
    tg.logger.setLevel(logging.DEBUG)
    bot.polling(non_stop=True, interval=0)
