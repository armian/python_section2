import pytube
import os
import subprocess

# 다운 받을 동영상 URL 지정
#yt = pytube.YouTube("https://www.youtube.com/watch?v=CTRO5NXmAp8")
yt = pytube.YouTube("https://www.youtube.com/watch?v=7ghhRHRP6t4")
videos = yt.streams.all()

for i in range(len(videos)) : # range(6)
    print(i, ' , ', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dirs = "/Users/armian/Inflearn/tmp/youtube"

videos[cNum].download(down_dirs)

subprocess.call(['cat','/etc/passwd'])

"""
mp4 -> mp3
여기서부터는 ffmpeg 외부 실행 명령어인데 윈도우즈 용이라서.. 커맨트 처리

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dirs,oriFIleName),
    os.path.join(down_dirs,newFileName)])
    
print("동영상 다운로드 및 mp3 변환 완료!")
"""
