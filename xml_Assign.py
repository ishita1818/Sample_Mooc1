import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location : ')
data = urllib.request.urlopen(url,context=ctx).read().decode()
print('Retrieving ',url)
tree = ET.fromstring(data)
comments = tree.findall('.//comment')
sum=0
for i in comments:
    sum+= int(i.find('count').text)

print('Retrieved ',len(data),' characters')
print('Count : ',len(comments))
print('Sum : ',sum)    
