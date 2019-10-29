# import pdb
# pdb.set_trace()
import os
# dane
monety =        [5, 2, 1, 0.5, 0.2, 0.1, 0]
monety_reszta = [0, 0, 0,   0,   0,   0]

banknot = 20
zakup = 8.30
reszta = banknot - zakup
# tekst = input('wpisz cos')

# indeks do trzymania pozycji listy
indeks_mon_reszta = 0

for moneta in monety:
    if reszta >= moneta:
        # ilosc = reszta // moneta
        try:
            ilosc = reszta // moneta
        except ZeroDivisionError:
            #print('dzielisz przez zero')
            continue
            # print(error)
        except NameError:
            continue
        # mozna napisac except (ZeroDivisionError, NameError): <- dziala jak or
        wartosc = ilosc * moneta
        reszta = reszta - wartosc
        # os.path.split('/home/')

        monety_reszta[indeks_mon_reszta] = ilosc

    indeks_mon_reszta += 1

print("Reszta do wydania:")