import urllib.request as dw

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150823_231%2Fcodn9_14403263840439uB4A_JPEG%2Ftumblr_n0forjSMuW1qgyg6yo1_540.jpg&type=sc960_832"
htmlURL = "http://google.com"

savePath1 = "/Users/armian/Inflearn/tmp/test1.jpg"
savePath2 = "/Users/armian/Inflearn/tmp/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
