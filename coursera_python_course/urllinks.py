# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# enter http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter URL: ')
counter = input('Enter count: ')
position = input('Enter position: ')

for i in range(int(counter)+1):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving: ', url)
    if i == (int(counter)):
        print(re.findall('[A-Z][a-z]*', url)[0])

    # Retrieve all of the anchor tags
    tags = soup('a')
    iter = 0

    for tag in tags:
        iter = iter + 1
        if iter == int(position):
            url = tag.get('href', None)




