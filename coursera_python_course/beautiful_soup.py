#The program will use urllib to read the HTML ,
# and parse the data, extracting numbers and compute the sum of the numbers in the file.


# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')

# Sum all the number contents of the tags
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])

print(sum)




