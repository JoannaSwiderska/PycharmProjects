text = 'Ala ma kota'
for char in text:
    print(char)

length = len(text)
for idx in range(length):
    print(text[idx])
    #z indeksami latwo sie machnac ze wyjdziemy poza obszar


some_range=range(length)
print(some_range)
is_loop_done = False
for value in some_range:
    print(value)
# else:
#   print("hello!")
    if value==length-1:
        is_loop_done = True
if is_loop_done:
    print("hello!")