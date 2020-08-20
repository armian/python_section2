from bs4 import BeautifulSoup
import re # regex

html="""
<html><body>
    <ul>
        <li><a id="naver" href="http://www.naver.com">naver</a><li>
        <li><a href="http://www.daum.net">daum</a><li>
        <li><a href="http://www.daum.com">daum</a><li>
        <li><a href="https://www.google.com">google</a><li>
        <li><a href="https://www.tistory.com">tistory</a><li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

# 기존에 배운 방
test = soup.find('a', string='naver')
print(test.string)

# ID 를 이용
test = soup.find(id='naver')
print(test.string)

# 정규표현식 이용
li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
    print(e.attrs['href'])

li2 = soup.find_all(href=re.compile(r"da"))
for e in li2:
    print(e.attrs['href'])
