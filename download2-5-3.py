
from bs4 import BeautifulSoup

html="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a><li>
        <li><a href="http://www.daum.net">daum</a><li>
        <li><a href="http://www.daum.com">daum</a><li>
        <li><a href="https://www.google.com">google</a><li>
        <li><a href="https://www.tistory.com">tistory</a><li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")

"""
print('links', type(links))
links <class 'bs4.element.ResultSet'>
"""

# 전체 가져오기
a = soup.find_all("a", string="daum")
print('a', a)

# 1개만 가져오기
b = soup.find("a")
print('b', b)

# 전체 갯수를 3개로 제한
b = soup.find_all("a", limit=3)
print('b', b)

# 해당 내용만 가져오기 (보통은 정규표현식을 넣어 준다)
c = soup.find_all(string=["naver","google"])
print('c', type(c), c)

for a in links:
    #print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    print('txt >> ', txt, 'href >> ', href)
