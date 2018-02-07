data=input('Podaj liczbe lub litere: ')

while not data.isdigit() and not data.isalpha():
    print('podales bledne dane')
    data = input('Podaj liczbe lub litere: ')

if data.isdigit():
    print('Podales liczbe')
elif data.isalpha():
    print('Podales litere')
print('bye!')
