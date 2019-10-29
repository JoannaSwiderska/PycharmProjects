# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.



import re

name = input("Enter file:")
handle = open(name)

lst = list()

for line in handle:
    findstr = re.findall('[0-9]+',line)
    for i in range(len(findstr)):
        numbr = int(findstr[i])
        lst.append(numbr)

print(sum(lst))