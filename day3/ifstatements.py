a=0
b=2.34
text='abc'

if b>a:
    print('b>a')
#if b<a:
#    print('b<a')
elif b==a:
    print('b=a')
else:
    print('b<a')

result=a>b
print(type(result))

if text:
    print('text is not empty')

x=1
y=2
z=3

if x<y<z:
    print('hurra')

# @TODO: if 'x'<'y'<'z'

something='abc'
another='xyz'

if something=='abc' and another=='xyz':
    print('strings are the same')

is_rest_equal_zero = 4 % 2

if not is_rest_equal_zero:
    print('the number is even')

name='Jan'
lastname='Kowalski'

if name=='Jan' or lastname=='Kowalski':
    print('siema!')
