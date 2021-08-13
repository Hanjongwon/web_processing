import urllib.request as req

ad_url1 = "https://ssl.pstatic.net/tveta/libs/1346/1346384/c119beefe64688e72f28_20210701100656742.png"
ad_url2 = "https://ssl.pstatic.net/tveta/libs/1351/1351368/0ec5c04ffde0779bcca7_20210804104506006.png"

save_path1 = "C:/Users/user/PycharmProjects/web_processing/ad1.jpg"
save_path2 = "C:/Users/user/PycharmProjects/web_processing/ad2.jpg"

req.urlretrieve(ad_url1, save_path1)
req.urlretrieve(ad_url2, save_path2)

print("네이버 광고 이미지 저장 완료")