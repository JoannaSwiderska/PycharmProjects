import os

FILENAME = 'dlugosc_pliku.txt'

file_size = os.path.getsize(FILENAME)
print(f'Rozmiar plik: {file_size}')


with open(FILENAME) as plik:
    #print(plik)
    total_chars = 0
    for line in plik:
        #linie z pliku
        total_chars += len(line)
    print(total_chars)


with open(FILENAME) as plik:
    print(plik.readlines())

