digits = {
    'cztery': 4,
    'dwa': 'dwa'
}

digit = input('Podaj liczbe: ')

    # try:
    #     result = digits[digit] - digits['dwa']
    # except Exception as error:
    #     print(f'ni ma takiego klucza jak: {error}')
    # finally:
    #     print('goodbye')

try:
    result = digits[digit] - digits['dwa']
except KeyError as keyerror:
    print(f'ni ma takiego klucza jak: {keyerror}')
    # pass <- do wyciszenia bledu ale bad practise
except TypeError as typeerror:
    print(f'ni ma takiego klucza jak: {typeerror}')
except Exception as excerror:
    print(f'mega fuckup: {excerror}')
finally:
    print('goodbye')
    # raise ValueError('hahaha sjbfafa')

