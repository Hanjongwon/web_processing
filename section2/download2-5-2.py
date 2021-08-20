from bs4 import BeautifulSoup


html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

print("html", html)

soup = BeautifulSoup(html, "html.parser")
#print("soup", type(soup))
# print("prettify", soup.prettify())

# h1 = soup.html.body.h1
# print("h1", h1)
p1 = soup.html.body.p
print("p1", p1)
p2 = p1.next_sibling.next_sibling
print("p2", p2)