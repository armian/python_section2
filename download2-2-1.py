import urllib.request as dw

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150823_231%2Fcodn9_14403263840439uB4A_JPEG%2Ftumblr_n0forjSMuW1qgyg6yo1_540.jpg&type=sc960_832"
htmlURL = "http://google.com"

savePath1 = "/Users/armian/Inflearn/tmp/test1.jpg"
savePath2 = "/Users/armian/Inflearn/tmp/index.html"

#urllib.request.urlretrieve(imgUrl, savePath)
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
