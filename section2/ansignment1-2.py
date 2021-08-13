import urllib.request as req

ad_url1 = "https://ssl.pstatic.net/tveta/libs/1346/1346384/c119beefe64688e72f28_20210701100656742.png"
ad_url2 = "https://ssl.pstatic.net/tveta/libs/1351/1351530/b8a428f4e2ae7e208e7a_20210720185106597.jpg"
save_path1 = "C:/Users/user/PycharmProjects/web_processing/ad1.jpg"
save_path2 = "C:/Users/user/PycharmProjects/web_processing/ad2.jpg"

f = req.urlopen(ad_url1).read()
f2 = req.urlopen(ad_url2).read()

with open(save_path1, "wb") as save_img1:
    save_img1.write(f)

with open(save_path2, "wb") as save_img2:
    save_img2.write(f2)
