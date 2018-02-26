
FILENAME = 'dlugosc_pliku.txt'

print('tryb do odczytu')
with open(FILENAME, 'r') as plik:
    cursor = plik.tell()
    print('pozycja kursora przed odczytem', cursor)
    print(plik.read())
    print('po odczycie')
    cursor = plik.tell()
    print(cursor)

# print('tryb do zapisu')
# with open(FILEAME, 'w') as plik:
#     print(plik.read())

# print('tryb dopisywania')
# with open(FILENAME, 'a') as plik:
#     plik.write('ala ma kota\n')


print('tryb dopisywania')
with open(FILENAME, 'a') as plik:
    cursor = plik.tell()
    print('pozycja kursora w trybie append', cursor)
    plik.seek(0)
    cursor = plik.tell()
    print('kursor przestawiony na pozycje:', cursor)
    plik.write('ala ma kota, kot ma ale\n')