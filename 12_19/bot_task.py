import telebot

bot = telebot.TeleBot("<TOKEN>")


@bot.message_handler(func=lambda message: message.text.lower().startswith("привет"))
def echo_welcome(message):
    bot.send_message(message.chat.id, "Тебе тоже привет!")


@bot.message_handler()
def send_welcome(message):
    bot.reply_to(message, str(message.json))


bot.infinity_polling()
