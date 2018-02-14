# program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# continue

for i in range(0,21,1):
    if i % 4:
        print(i)
    else:
        continue

# program obliczajacy liczbe liter i cyfr w stringu

strng="Tomek36"
ilosc_znakow = str(len("Tomek36"))
print(ilosc_znakow)

ilosc_liter=0
ilosc_cyfr=0

for char in strng:
    if char.isalpha():
        ilosc_liter += 1
    elif char.isdigit():
        ilosc_cyfr += 1

print('liter: ', ilosc_liter, ' liczb: ', ilosc_cyfr)


# program wypisujący tabliczkę mnozenia (1 do 10) dla podanej przez użytkownika liczby
# np: 3 x 1 = 3
#     3 x 2 = 6
#     3 x 3 = 9 itp


value = input('Podaj liczbe rozna od zera: ')

while not value.isdigit() or int(value)==0:
    print('podales bledne dane')
    value = input('Podaj liczbe rozna od zera: ')

value = int(value)

for n in range(1,(value+1),1):
    wynik = value*n
    print(value, ' x ', n, ' = ', wynik)


# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata


#wpisz wiek psa
# wiek_psa = int(input("Podaj wiek psa?: "))
# wiek2 = wiek_psa * 4 - 8
#
# #jesli 1 lub 2 to x10,5
# if wiek_psa < 3:
#     wiek = wiek_psa * (10.5)
#     print("Twoj pies ma {} lat".format(wiek))
#
# elif wiek_psa > 2:
#      wiek_staregopsa = wiek2 + 21
#      print("Twoj pies jest stary i ma {} lat".format(wiek_staregopsa))

#jesli 3 lub wiecej to x4
#podaj wiek w ludzkich latach


wiek_psa = int(input("Podaj wiek psa?: "))
wiek_psa_przeliczony = 0

#jesli 1 lub 2 to x10,5
if wiek_psa < 3:
    wiek_psa_przeliczony = wiek_psa * (10.5)

elif wiek_psa > 2:
    wiek_psa_przeliczony = 21 + (wiek_psa - 2) * 4

print("Twoj pies ma {} psich lat".format(wiek_psa_przeliczony))