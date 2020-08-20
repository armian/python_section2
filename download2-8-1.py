from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote
print (url)

res = req.urlopen(url)

savePath = "/Users/armian/Inflearn/imagedown"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실퍠!")
        raise

soup = BeautifulSoup(res, "html.parser")

#print(soup)

img_list = soup.select("div.img_area > a.thumb._thumb > img")

print("test", img_list)

for i, img_list in enumerate(img_list, 1):
    #print(i, img_list['data-source'])
    #fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    fullFileName = os.path.join(savePath, str(i)+'.jpg')
    print(fullFileName)
    req.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료")
