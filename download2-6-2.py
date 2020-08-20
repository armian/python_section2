from bs4 import BeautifulSoup

# food-list.html -> '양주' 가져오기

fp = open("./food-list.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")
fp.close()

"""
x = soup.select_one("li:nth-of-type(5)")
print(x)
"""

# 아래 식이 안되는 이유를 모르겠음 ㅠㅠ
#print("1", soup.select_one("li:nth-of-type(8)").string)

print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("4", soup.select("#ac-list > li.alcohol.high")[0].string)

param = {"data-lo":"cn", "class":"alcohol"}
print("5", soup.find("li", param).string)
print("6", soup.find(id="ac-list").find("li", param).string)

for ac in soup.find_all("li"):
    print(ac)
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
