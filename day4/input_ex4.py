value=input('Podaj liczbe rozna od zera: ')

while not value.isdigit() or int(value)==0:
    print('podales bledne dane')
    value = input('Podaj liczbe lub litere: ')

print('Podales liczbe')

