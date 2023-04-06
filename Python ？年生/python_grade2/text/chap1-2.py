import requests

url="https://www.ymori.com/books/python2nen/test1.html"
response=requests.get(url)

response.encoding=response.apparent_encoding

fn="download.txt"
f=open(fn, mode="w")

f.write(response.text)

f.close()