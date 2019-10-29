class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def mowi(self):
        print('zwierze nie mowi')

    def __str__(self):
        return str(self.imie).capitalize()

class Kon(Zwierze):
    def __init__(self, imie):
        Zwierze.__init__(self,imie)

    def mowi(self):
        print('iha')

    def skacz(self):
        print('Kon skacze')


class Osiol(Zwierze):
    def __init__(self, imie):
        Zwierze.__init__(self,imie)

    def mowi(self):
        print('ihaaa jestem osiol')

    def biegnij(self):
        print('Ja nie biegam, jestem osiol')

class Mul(Osiol, Kon):
    pass


print('\nZwierzak: ------------------')
# tworzymy instancje Zwierze
animal1 = Zwierze('zwierzak')
print(animal1)
animal1.mowi()

print('\nKoń: ------------------')
# tworzymy instancje Kon
kon1 = Kon('Kary')
print(kon1)
# jak widzimy kon korzysta z wlasnej implementacji
kon1.mowi()
kon1.skacz()

print('\nOsioł: ------------------')
osiol1 = Osiol('donkey kong')
osiol1.mowi()
osiol1.biegnij()


print('\nMul: ------------------')
mul1=Mul('Mulek')
mul1.mowi()

mul1.skacz()
mul1.biegnij()