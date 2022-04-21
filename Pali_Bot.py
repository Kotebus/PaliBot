import telebot
import requests
import random
from bs4 import BeautifulSoup

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
    result = []
    with open("sitemap.xml", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, features="xml")
        for tag in soup.find_all("loc"):
            result.append(tag.text)

    sn = random.randint(1, len(result))
    url = result[sn]

    resp = requests.get(url)
    resp.encoding = "windows-1251"

    name = ""
    apo = ""
    text_sutta = ""

    y = BeautifulSoup(resp.text, "lxml")
    for a in y.select('table td[height="36"] font[face="Times New Roman, Times, serif"][size="5"]'):
        name += a.text
    
    for a in y.select('font[color="#996633"]'):
        apo = a.text + text_sutta

    for tag in y.select('font[face="Arial, Helvetica, sans-serif"][size="2"]'):
        text_sutta = text_sutta + tag.text
    
    lis_name = name.split()  
    my_name = " " .join(lis_name)
    
    t = apo+text_sutta
    lis_t = t.split()
    my_text = " ".join(lis_t)
    print_text = my_name+"\n\n"+my_text

    bot.send_message(message.chat.id, print_text + '\n\n>>> СЛЕДУЮЩАЯ СУТТА:  /next_sutta')

bot.polling(none_stop=True)	
