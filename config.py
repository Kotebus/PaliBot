import requests
import random
from bs4 import BeautifulSoup

########################################################

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
    my_name = " ".join(lis_name)

    t = apo + text_sutta
    lis_t = t.split()
    my_text = " ".join(lis_t)
    print_text = my_name + "\n\n" + my_text
    return print_text



