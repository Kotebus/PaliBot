import requests
import random
from bs4 import BeautifulSoup

########################################################
def clean_text(text):
    return ' '.join(text.replace('\r\n', '').replace('\n\n', '\n').split())

def mainconfig(xmlfile):
    result = []
    with open(xmlfile, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, features="xml")
        for tag in soup.find_all("loc"):
            result.append(tag.text)

    sn = random.randint(0, len(result) - 1)
    url = result[sn]

    resp = requests.get(url)
    resp.encoding = "windows-1251"

    main_text = ""

    response = BeautifulSoup(resp.text, "lxml")

    title_tag = response.select('table [width="70%"] td font font')[0]
    title = clean_text(title_tag.text)

    for node in response.select('table td[style="text-align: justify"]'):
        main_text += node.text

    return clean_text(title) + '\n' + clean_text(main_text) + '\n' + url
