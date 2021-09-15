import requests

s = requests.Session()
r = s.get('http://httpbin.org/get')
# print(r.status_code)
# print(r.ok)

#https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/album0s')
#print(r.text)
print(r.json())
