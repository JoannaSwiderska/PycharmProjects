# import sys
# from pprint import pprint
# import test
#Cfrom package_example.test import *
from package_example.functions import hello

pprint(sys.path)
print(test)

data = input('Podaj imie: ')

print(hello(data))
print('globals', globals())
