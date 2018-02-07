numbers = input('Podaj strat, stop i step (w formacie START,STOP,STEP): ')

while int(numbers.split(",")[0]) >= int(numbers.split(",")[1]):
    print('start ma byc mniejszy niz stop')
    numbers = input('Podaj strat, stop i step (w formacie START,STOP,STEP): ')

start = int(numbers.split(",")[0])
stop = int(numbers.split(",")[1])
step = int(numbers.split(",")[2])

count_even=0
count_noteven=0

for i in range(start, stop+1, step):
    if i % 2:
        count_noteven += 1
    else:
        count_even += 1

print('parzystych: ', count_even, ' nieparzystych: ', count_noteven)