class Silnik:
    def __init__(self, pojemnosc, typ, liczba_koni_mech, uruchomiony=False):
        self.pojemnosc = pojemnosc
        self.typ = typ
        self.liczba_koni_mech = liczba_koni_mech
        self.uruchomiony = uruchomiony

    def __str__(self):
        return f'Silnik o pojemnsci: {self.pojemnosc}, typie: {self.typ} i liczbie koni mechanicznych: {self.liczba_koni_mech}.' \
               f'Czy jest uruchomiony? {self.uruchomiony}'

    def uruchom_silnik(self):
        self.uruchomiony = True

    def wylacz_silnik(self):
        self.uruchomiony = False

    def increase_hp(self, amount):
        self.liczba_koni_mech += amount




class Samochod:
    def __init__(self, marka, model, silnik=None):
        self.marka = marka
        self.model = model
        self.silnik = silnik

    def __str__(self):
        return f'Samochod marki {self.marka} model {self.model} ma silnik: {self.silnik}'

    def __len__(self):
        return len(self.marka)

    def boost(self,amount):
        self.silnik.increase_hp(amount)



# class Samochod:
#     def __init__(self, marka, model, start = False):
#         print('wywoluje __init__')
#         self.marka = marka
#         self.model = model
#         self.uruchomiony = start


if __name__ == '__main__':
    v8 = Silnik(5.7, 'petrol', 400)
    jeep = Samochod('Jeep', 'Cheeroke', v8)
    print(jeep)
    # ponizej zwracamy dlugosc marki
    # print(len(jeep))
    jeep.boost(100)
    print(jeep)

# if __name__ == '__main__':
#     print('przed utworzeniem instancji')
#
#     golf = Samochod('Volkswagen', 'Golf')
#     print('po utworzeniu instancji')
#     print(golf.marka, golf.model, golf.uruchomiony)
#     print(golf)
#     golf.uruchom_samochod()
#     # print(golf.uruchomiony)
#     print(golf)
#
#     megane = Samochod('Renault', 'Megane', start=True)
#     print(megane.marka, megane.model, megane.uruchomiony)
#     print(megane)
#     megane.wylacz_samochod()
#     #  print(megane.uruchomiony)
#     print(megane)
