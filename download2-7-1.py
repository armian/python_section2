from bs4 import BeautifulSoup
import urllib.request as req
import requests

"""
url = "http://finance.daum.net/domestic/market_cap"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
"""

html = requests.get("http://finance.daum.net/domestic/market_cap")
soup = BeautifulSoup(html.text, "html.parser")

#print('soup', soup.prettify())

#top = soup.select("#boxMarketCap > div.box_contents > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a")
top = soup.select("#boxMarketCap > div.box_contents")

print(top)
