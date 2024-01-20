import random
import telebot

Token = ""

bot = telebot.TeleBot(Token)

@bot.message_handler(['quote'])
def start(msg):
    try:
        print("hello aman")
        with open('quotes.txt', 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)

        bot.reply_to(msg,random_line)
    except Exception as e:
        print(e)
        bot.reply_to(msg, "Oops!server is busy try again ")

bot.polling()
