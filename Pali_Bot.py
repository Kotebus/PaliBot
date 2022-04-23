import telebot
from config import mainconfig

########################################################

token = '5317155773:AAGm4aujvEWBcm2AVWsCzHM_RYQh-_cYwa8'
bot = telebot.TeleBot(token)

main_menu = """
Добро пожаловать в тестовую версию бота - 
открывающего случайные сутты из Палийского Канона.

Для продолжения нажмите:
>>> /all_sutta - ИЗ ВСЕХ СУТТ
>>> /theragatha_sutta - ИЗ ТХЕРАГАТХИ"""

@bot.message_handler(commands=['start'])
def main_menuu(message):
    bot.send_message(message.chat.id, main_menu)\

@bot.message_handler(commands=['all_sutta'])
def all_suttaa(message):
    print_text = mainconfig("sitemap.xml")
    bot.send_message(message.chat.id, print_text + '\n\n>>> СЛЕДУЮЩАЯ СУТТА:  /all_sutta\n>>> МЕНЮ: /start')

@bot.message_handler(commands=['theragatha_sutta'])
def theragatha_suttaa(message):
    print_text = mainconfig("sitemap_theragatha.xml")
    bot.send_message(message.chat.id, print_text + '\n\n>>> СЛЕДУЮЩАЯ СУТТА:  /theragatha_sutta\n>>> МЕНЮ: /start')

bot.polling(none_stop=True)	
