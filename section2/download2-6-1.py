from bs4 import BeautifulSoup
import re

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">good</a></li>
        <li><a href="https://www.tistory.com">tistory></a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
li = soup.find_all(href=re.compile(r"^https://"))

for e in li:
    print(e.attrs["href"])