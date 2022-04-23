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

    sn = random.randint(1, len(result))
    url = result[sn]

    resp = requests.get(url)
    resp.encoding = "windows-1251"

    main_text = ""
    title = ""

    response = BeautifulSoup(resp.text, "lxml")

    for node in response.select('table [width="70%"] td font font'):
        title += node.text

    # title = clean_text(response.select('table [width="70%"] td')[5].text)

    for node in response.select('table td[style="text-align: justify"]'):
        main_text += node.text

    return title + '\n' + clean_text(main_text) + '\n' + url
