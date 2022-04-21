import telebot
from config import mainconfig

########################################################

token = '5317155773:AAGm4aujvEWBcm2AVWsCzHM_RYQh-_cYwa8'
bot = telebot.TeleBot(token)

main_menu = """
Добро пожаловать в тестовую версию бота - 
открывающего слечайные сутты из Палийского Канона.

Для продолжения нажмите:
>>> /next_sutta"""

@bot.message_handler(commands=['start'])
def main_menuu(message):
    bot.send_message(message.chat.id, main_menu)\

@bot.message_handler(commands=['next_sutta'])
def next_suttaa(message):
    print_text = mainconfig("sitemap.xml")
    bot.send_message(message.chat.id, print_text + '\n\n>>> СЛЕДУЮЩАЯ СУТТА:  /next_sutta')

bot.polling(none_stop=True)	
