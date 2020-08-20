from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
#print(quote)

url = base + quote

res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parser")

#print(soup)

recommand = soup.select("ul.slides")[0]
print(recommand)

for e in recommand:
    print(e.select_one("h4.block_title > a"))
