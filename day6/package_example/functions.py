def hello(username):
    """

    :param username:
    :return:
    """
    # return username.upper()
    name = username.upper()
    print('locals', locals())
    return name

name = 'Ania'
lastnme = 'Kowalska'
# print(__name__)
if __name__=='__main__':
    print(hello(name))
    print('globals', globals())