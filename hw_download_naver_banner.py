import urllib.request as dw

imgUrl = "https://ssl.pstatic.net/tveta/libs/1289/1289698/bc7ff718d4d751061acb_20200813113356186.jpg"
mp4Url = "https://tvetamovie.pstatic.net/libs/1294/1294508/1abdda4d995c546b2b00_20200812115831356.mp4-pBASE-v0-f110102-20200812120343756.mp4"

savePath1 = "/Users/armian/Inflearn/tmp/naver_banner.jpg"
savePath2 = "/Users/armian/Inflearn/tmp/naver_banner.mp4"

#urllib.request.urlretrieve(imgUrl, savePath)
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(mp4Url, savePath2)

print("다운로드 완료!")
