import xml.etree.ElementTree as ET
data = '''<person>
    <name>Ishita Sharma</name>
    <phone type ="intl">
        +91 9467161455
     </phone>
     <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name : ',tree.find('name').text)
print('Attr : ',tree.find('email').get('hide'))