import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=wkVlb8rSies") #다운 받을 동영상 URL 저장
videos = yt.streams

#print("videos", videos)

for i in range(len(videos)):
    print(i, ', ', videos[i])

cNum = int(input("다운 받을 화질은?"))
down_dir = "C:/Users/user/PycharmProjects/web_processing/youtube"

videos[cNum].download(down_dir)