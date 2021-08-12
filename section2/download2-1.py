import urllib.request as dw

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MTdfMTM1%2FMDAxNjIxMjUwMzk5MTM2.Fjl5w5-w6WNGAoZevYxGj_hkcCVK-q4kfuIUn_em0wgg.KIwAeOkgXXDn0DDvHperUTI2pBa-B8Tras6j_tybdxUg.JPEG.addpm%2F%25B5%25B9%25BA%25BD-4.jpg&type=sc960_832"
htmlURL = "https://www.google.co.kr/"

savePath1 = "C:/Users/user/PycharmProjects/web_processing/test1.jpg"
savepath2 = "C:/Users/user/PycharmProjects/web_processing/index.html"
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savepath2)
print("다운로드 완료!")