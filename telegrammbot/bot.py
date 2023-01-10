import telebot

bot = telebot.TeleBot("5901080060:AAGwl8wMR8lHsv6JSRZYrIXN21-WKGuC1lY")
@bot.message_handler(commands=["start"])
def start (msg):
    print(msg)
    bot.send_message(chat_id = msg.chat.id, text = "Это игра Крестики нолики, добро пожаловать!")
bot.polling()
