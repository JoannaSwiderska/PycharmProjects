name = 'Ola'

def hello(username):
    """

    :param username:
    :return:
    """
    # jesli zdefiniujemy name globalnie to nadpisze OLA z podanym imieniem
    global name
    name = username.upper()
    return name

data = input('Podaj imie: ')
uppercased = hello(data)
print(uppercased)
print(name)