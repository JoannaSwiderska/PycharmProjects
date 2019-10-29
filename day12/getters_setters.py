# @TODO: klasa Person
# @TODO: attr: imie, nazw, miasto, miasto2, kod_pocztowy, sdres jako attr ukryty
# @TODO: "Jakaswies 144, 12-345 Miasto Gminne"
# @TODO: "Wadowicka 6d, 30-415 Krakow"
# @TODO: p.adres -> "Wadowicka 6d, 30-415 Krakow"
# @TODO: p2.adres -> "Jakaswies 144, 12-345 Miasto Gminne"
# @TODO: f'{Ulica}|{miasto} {nr}, {kod} {miasto}|{miasto2}'
# @TODO: uzyc funkcji all([miasto,miasto2])


class Person:
    def __init__(self, imie, nazw, ulica='', nr='', miasto='', misto_gm='', kod=''):
        self.imie = imie
        self.nazwisko = nazw
        self.ulica = ulica
        self.nr_domu = nr
        self.miasto = miasto
        self.misto_gminne = misto_gm
        self.kod_pocztowy = kod
        self.__adres = ''

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.ulica} {self.nr_domu} {self.miasto} {self.misto_gminne} {self.kod_pocztowy}'

    @property
    def adres(self):
        if self.ulica:
            return f'{self.ulica} {self.nr_domu} {self.miasto} {self.kod_pocztowy}'
        else:
            return f'{self.miasto} {self.nr_domu} {self.misto_gminne} {self.kod_pocztowy}'




if __name__=='__main__':
    jan= Person(
        'Jan', 'Kowalski', 'Wadowicka', '6d', 'Krakow', 'Krakow', '30-415'
    )
    adam = Person(
        'Adam', 'Nowak', nr='144', miasto='Wies', misto_gm='Miasto', kod='12-345'
    )

    print(jan.adres)
    print(adam.adres)




