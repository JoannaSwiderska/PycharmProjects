# import math

# print(dir(math))

a=1
b=2
c=7

result=a+b
print(result)

result=a-b
print(result)

result=a*2
print(result)

result=c/b
print(result)

result=c//b # zaokraglenie w dol
print(result)

z=4.23


print(type(b))
print(type(z),z)

z_int=int(z)

print(type(z_int),z_int)

# @TODO: sprawdzic jak dziala ^
result=b^4
print(result)

#print('before',c)
#c += 2
#c -= 5
#c *= 4
#c /= 6
#print('after',c)

c = c % 2 # c modulo 2
print(c)

text= "Ala ma kota" # mozna podwojny i pjedynczy cudzyslow
eng= "Tom's home" # tu lepiej podwojny bo pojedynczy mamy w tekscie
print(eng)
eng2= 'Tom\'s house'
print(eng2)

#two = 2
#zero = 0
#print(two / zero)


letter_a=text[2]
last_char=text[-1]
print(letter_a)
print(last_char)
length=len(text)
print(length)
last_char_2=text[length - 1] #samo length da blad ze index out of range
print(last_char_2)

something=text[3:6]
print(something)
something2=text[-4:-1]
print(something2)
steps=text[0:10:2]
print(steps)
print(text[0:15])
dunno=text[0:15]
print(dunno)
print(id(text))
print(id(dunno))

text2=text[::-1]
print(text2)

print(text.upper())
print(text.lower())
print(text.capitalize())

#text[0]='O' # nie ma operacji przypisania dla stringow
text = 'O' + text[1:]
print(text)
text = text[:4] + 'M' + text[5:]
print(text)

text3="Ala ma kot,kot bardzo lubi Ale"
old='kot'
new='pies'
count=1
replaced=text3.replace(old,new,count) #count mowi w tym ktore wystapienie
print(replaced,id(replaced))
print(text3,id(text3))