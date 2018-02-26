with open('osoby') as plik:
    header = plik.readline()
    header = header.strip()
    name, last_name, age = header.split(',')
    #print(header)
    print(f'{name} | {last_name} | {age}')
    print('*****')
    for line in plik:
        print(line.strip()) #strin pozbywa sie white spaces jak trim
#
# with open('osoby', 'a') as plik:
#     nowe_dane = input('Podaj imie, nazwisko i wiek (w formacie np.JAN KOWALSKI 40): ')
#     imie = nowe_dane.split(" ")[0]
#     nazwisko = nowe_dane.split(" ")[1]
#     wiek = nowe_dane.split(" ")[2]
#     plik.write(f'{imie},{nazwisko},{wiek}\n')


# FORMAT = '{imie},{nazwisko},{wiek}\n'
#     imie = input('Podaj imie: ')
#     nazwisko = input('Podaj nazwisko: ')
#     wiek = input('Podaj wiek: ')
#
# with open('osoby', 'a') as plik:
#     plik.write(FORMAT.format(imie=imie,nazwisko=nazwisko,wiek=wiek))


data = ['Jan', 'Kowalski', '33']
#plik.write nie przekaze listy, musi byc string


import csv

with open('osoby') as plik:
    reader = csv.reader(plik)
    for line in reader:
        print(reader)


with open('osoby', 'a') as plik:
    writer = csv.writer(plik)
    writer.writerow(data)