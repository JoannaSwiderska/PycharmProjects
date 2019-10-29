people = {
    'kowalski': 'jan',
    'nowak': 'adam'
}

last_name = input('Podaj nazwisko: ')

# # bad
# if last_name in people:
#     print(people[last_name])
#
# # better
# message = 'Nazwisko nie istnieje w bazie'
# print(people.get(last_name,message))

# the best
# try:
#     print(people[last_name])
# except KeyError as keyerr:
#     print(f'Nie ma takiego nazwiska jak: {keyerr}')




filename = input('Podaj nazwe pliku: ')

try:
    plik = open(filename)
    print(plik.read())
except FileNotFoundError as error:
    print(f'Pliku nie znaleziono: {error.filename}')
finally:
    print('goodbye')
# finally:
#     plik.close()