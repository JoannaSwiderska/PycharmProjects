# while True:
#     print('Hello!')

counter = 0
value = input('Podaj liczbe: ')
value = int(value)

# while counter < value:
#     print ('Hello!')
#     counter += 1
# # ten warunek jest juz poza petla
# print('Bye')



# @TODO: wywietl counter tylko jesli jest niearzysty

# while counter < value:
#     if counter % 2:
#         print(counter)
#         counter += 1
#     else:
#         counter += 1
#         continue
#
# # ten warunek jest juz poza petla
# print('Bye')


while counter < value:
    if counter % 2:
        print(counter)
        counter += 1
    elif value > 1000:
            break
    else:
        counter += 1
        continue

# ten warunek jest juz poza petla
print('Bye')



