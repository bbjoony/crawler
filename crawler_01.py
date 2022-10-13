import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'http://quotes.toscrape.com/'
html = ur.urlopen(url)

soup = bs(html.read(), 'html.parser')

pretext = soup.find_all('div', {"class" : "quote"}) #배열 형태로 반환
# print(pretext[0].text)

for i in pretext:
    print(i.text)