# The program will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
# It's second solution to urllinks_2.py

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
#http://py4e-data.dr-chuck.net/comments_42.xml

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data.decode())


counts = tree.findall('.//count')
cnt = 0
sm = 0


for nmbr in counts:
    cnt = cnt + 1
    sm = sm + int(nmbr.text)


print('Count:', cnt)
print('Sum:', sm)