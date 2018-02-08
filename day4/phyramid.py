levels = input('Podaj liczbe poziomow piramidy (dodatnia liczba calkowita): ')

while not levels.isdigit() or int(levels)==0:
    print('podales zla wartosc')
    levels = input('Podaj liczbe poziomow piramidy (dodatnia liczba calkowita): ')


print()
for i in range(1, int(levels)+1):
    print(' '*(int(levels)-i), '#'*(2*i-1), ' '*(int(levels)-i))