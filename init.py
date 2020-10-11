import telebot
import private

bot = telebot.TeleBot(private.TOKEN)


@bot.message_handler(regexp="Го бухать?")
def go(message):
    bot.reply_to(message, 'Го!')


@bot.message_handler(regexp="Пидор")
def go(message):
    bot.reply_to(message, 'Сам пидор')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ты че дурак? Зачем ты сюда лезешь?")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Тест команды /help в боте")







bot.polling()
