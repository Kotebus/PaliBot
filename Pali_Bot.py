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
>>> /dhammapada_sutta - ИЗ ДХАММАПАДЫ
>>> /theragatha_sutta - ИЗ ТХЕРАГАТХИ"""

def get_text(sitemap, command):
    try:
        print_text = mainconfig(sitemap)
    except Exception as e:
        print_text = e

    return print_text + '\n\n>>> СЛЕДУЮЩАЯ СУТТА:  /' + command + '\n>>> МЕНЮ: /start'

@bot.message_handler(commands=['start'])
def main_menuu(message):
    bot.send_message(message.chat.id, main_menu) \

@bot.message_handler(commands=['all_sutta'])
def all_suttaa(message):
    print_text = get_text("sitemap.xml", 'all_sutta')
    bot.send_message(message.chat.id, print_text)

@bot.message_handler(commands=['theragatha_sutta'])
def theragatha_suttaa(message):
    print_text = get_text("sitemap_theragatha.xml", 'theragatha_sutta')
    bot.send_message(message.chat.id, print_text)

@bot.message_handler(commands=['dhammapada_sutta'])
def dhammapada_suttaa(message):
    print_text = get_text("sitemap_dhammapada.xml", 'dhammapada_sutta')
    bot.send_message(message.chat.id, print_text)


bot.polling(none_stop=True)
