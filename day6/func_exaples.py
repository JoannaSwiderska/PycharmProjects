# def infinite_arguments(*args):
#     print(args)
#     print(type(args))
#
# print(sum([1, 2]))
#
# #funkcja ktora przyjmuje dowolna liczbe arg liczbowyh i wyswietla ich sume na ekranie
# def improved_sum(*args):
#     print(sum(args))
#
# improved_sum(1, 2, 3, 4, 5, 7)
# #z lista nie poradzi sobie zeby rozpoznac argumenty dlatego dodajemy *
# improved_sum(*[1, 2, 3])
#
# x, y, z, *something = (1, 2, 3, 4, 5, 6)
# print(x)
# print(y)
# print(z)
# print(something)
# *nevermind, a, b = (1, 10, 20, 30, 40)
# print(nevermind)
# print(a, b)
#
#
# def foo(a, b, *args):
#     """
#     Function simply prints the arguments
#     :param a:
#     :param b:
#     :param args:
#     :return:
#     """
#     print(a, b, args)
#
# foo(1, 2)
# foo(1, 2, 3, 4, 5, 6)
# foo(1, 2, *range(10))
#
# # w ** mozemy przekazywac slowniki , przydatne przy dowolnej liczbie zmiennych nazwanych
# def bar(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}-> {value}')
#
# bar(a=1, b=2, zxc=4)
# my_dict = {'Kowalski': 123, 'Nowak': 456}
# bar(**my_dict)

def baz(x, y, **kwargs):
    pass

def improved_sum_with_return(*args):
    """
    Sum only number
    :param args:
    :return:
    """
    return sum(args)


values_to_sum = [1, 2, 10, 15]
result = improved_sum_with_return(*values_to_sum)
print(result)

def compare(a, b):
    """
    Return true if a>b
    :param a:
    :param b:
    :return:
    """
    return a > b


print(compare(1, 2))
print(compare(4, 2))

# @TODO: ponizszy kod zamien na funkcje validate_input

# while not data.isdigit() and not data.isalpha():
#     print('podales bledne dane')
#     data = input('Podaj liczbe lub litere: ')


