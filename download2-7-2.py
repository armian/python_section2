from bs4 import BeautifulSoup
import urllib.request as req
import requests

html = requests.get("https://finance.naver.com/sise/")
soup = BeautifulSoup(html.text, "html.parser")

#print('soup', soup.prettify())

top10 = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top10:
    if e.find("a") is not None:
        print(i,e.select_one(".title").string)
        i += 1
