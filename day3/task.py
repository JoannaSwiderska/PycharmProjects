digit = input('Podaj liczbe: ')

# zmiana stringu na integer
digit = int(digit)

digit_mod_2 = digit % 2

if digit_mod_2 == 0:
    is_even = 1
else:
    is_even = 0


if is_even:
    print('liczba jest parzysta')
else:
    print('liczba nie jest parzysta')

