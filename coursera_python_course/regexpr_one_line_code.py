# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# Try to write the code in smallest number of code lines possible.


import re

print(sum(int(el) for el in re.findall('[0-9]+', open(input("Enter file:")).read())))






