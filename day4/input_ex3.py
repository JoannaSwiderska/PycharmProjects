is_digit_or_alpha = False

while is_digit_or_alpha == False:
    data = input('Podaj liczbe lub litere: ')
    if data.isdigit():
        print('Podales liczbe')
        is_digit_or_alpha = True
    elif data.isalpha():
        print('Podales litere')
        is_digit_or_alpha = True
    else:
        print('jesczze raz!!!')
