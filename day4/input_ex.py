data=input('Podaj liczbe lub litere: ')

if data.isdigit():
    print('Podales liczbe')
    print('bye!')
elif data.isalpha():
    print('Podales litere')
    print('bye!')
else:
    print('Help!!!')

