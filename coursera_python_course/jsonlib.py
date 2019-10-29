# The program will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
# http://py4e-data.dr-chuck.net/comments_42.json

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

#print(json.dumps(js,indent=4))
sm = 0
cnt = 0

for i in range(0, len(js["comments"])):
    cnt = cnt + 1
    sm = sm + int(js["comments"][i]["count"])


print('Count:', cnt)
print('Sum:', sm)