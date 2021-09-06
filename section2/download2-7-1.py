from bs4 import BeautifulSoup
import urllib.request as req
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
        'User-Agent' : ua.ie,
        'referer' : 'https://finance.daum.net/'
}



# print("soup", soup.prettify())

top = soup.select("ul#list > li")
print(top)
