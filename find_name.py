from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Count - ')
pos = input('Position - ')

name=""
for i in range(int(count)):
    print('Retrieving : ',url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    tag = tags[int(pos)-1]
    name = tag.contents[0]
    url = tag.get('href',None)

print(name)