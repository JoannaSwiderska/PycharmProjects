phonebook = {
    'Kowalski':123,
    'Nowak':456,
    'Isinski':879
}


# lastname=input('Podaj nazwisko: ')
# print(phonebook[lastname])

lastname='XYZ'
print(phonebook.get(lastname,'Brak takiego nazwiska'))


new_phonebook=phonebook.copy()
print(new_phonebook)
new_members={'XYZ':1,'ABC':2}
new_phonebook.update(new_members)
print(new_phonebook)

new_phonebook['XYZ']=0
print(new_phonebook)

new_phonebook.update({'XYZ':5})
print(new_phonebook)

new_phonebook.update(Kowalski=898,Nowak=111)
print(new_phonebook)

del new_phonebook['XYZ']
print(new_phonebook)
new_phonebook['abrcadabra']=[123,456,789]

for element in new_phonebook:
    print(element)


for key,element in new_phonebook.items():
    print(f'{key}->{element}')

only_keys=new_phonebook.keys()
print(only_keys)
values=new_phonebook.values()
print(values)
items=new_phonebook.items()
print(items)


