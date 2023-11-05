import requests
from bs4 import BeautifulSoup

def extract_text(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_=class_name)
    texts = [element.text for element in elements]
    return texts

url = 'https://www.umegaoka.net/shop/list.html'
class_name = 'mediabody'
texts = extract_text(url, class_name)
print(texts)
