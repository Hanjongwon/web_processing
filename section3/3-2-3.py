import requests, json

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream=True)
#print(r.text)
#print(r.encoding)
#print(r.json())

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    b = json.loads(line)
    print(type(b))

    for e in b.keys():
        print("keys:", e, 'values:', b[e])