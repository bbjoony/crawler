import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir(r'/Users/devsiters/Documents/GitHub/crawler/docs')

news = 'https://news.daum.net'
soup = bs(ur.urlopen(news).read(), 'html.parser')

for i in soup.find_all('div', {"class":"item_issue"}):
    print(i.text)    