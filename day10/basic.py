class Zwierze:
    def __init__(self, l_konczyn, typ, pozywienie, rozmnazanie, wiek):
        self.liczba_konczyn = l_konczyn
        self.typ_poruszania = typ
        self.typ_pozywienia = pozywienie
        self.typ_rozmnazania = rozmnazanie
        self.wiek = wiek
        self.__foo = 0

    def hello(self):
        return 'zwierze'

    def bar(self):
        self.__foo = 3

class Czlowek(Zwierze):
    # * wmusza ze dla wartosci domyslnej jesli podajemy wartosc nowa to musimy okreslic nazwe tej zmiennj
    # np. l_konczyn = 5 a nie samo 5 po przecinku
    # def __init__(self, rasa, wiek, *, l_konczyn=4, typ='chodzacy', pozywienie='wszystkozerne', rozmnazanie='zyworodne'):
    def __init__(self, rasa, wiek, *, l_konczyn=4, typ='chodzacy', pozywienie='wszystkozerne')
        # ukrywamy ten attrybut przed uzytkownikim
        self.__typ_rozmnazania = 'zyworodne'
        super().__init__(l_konczyn, typ, pozywienie, rozmnazanie, wiek)
        self.rasa = rasa

    def hello(self):
        return 'czlowiek'

    def goodbye(self):
        self.__typ_rozmnazania = 'something'

# class Czlowek(Zwierze):
#     def __init__(self, l_konczyn, typ, pozywienie, rozmnazanie, rasa):
#         # self.liczba_konczyn = l_konczyn
#         # self.typ_poruszania = typ
#         # self.typ_pozywienia = pozywienie
#         # self.typ_rozmnazania = rozmnazanie
#         super().__init__(self, l_konczyn, typ, pozywienie, rozmnazanie)
#         self.rasa = rasa

class Student(Czlowek):
    def __init__(self, rok, kierunek, wiek, imprezowicz, rasa='biala'):
        super().__init__(rasa, wiek)
        self.rok = rok
        self.kiernek = kierunek
        self.imprezowicz = imprezowicz

    def hello(self):
        return 'student'

if __name__ == '__main__':
    # zwierze = Zwierze(3, 'pelzajace', 'wszystkozerne', 'zyworodne')
    # czlowiek = Czlowek(4, 'chodzacy', 'wszystkozerne', 'zyworodne', 'biala')
    # czlowiek = Czlowek('biala')
    # print(zwierze.liczba_konczyn, zwierze.typ_poruszania)
    # print(czlowiek.liczba_konczyn, czlowiek.typ_poruszania, czlowiek.rasa)
    # print(dir(zwierze))
    # print(dir(czlowiek))
    student = Student(3, 'IT', 22, False)
    czlowiek = Czlowek('biala', 23)
    zwierze = Zwierze(2, 'latajacy', 'rosliny', 'jajorodny', 1)
    # print(student)
    # print(isinstance(student, Student))
    # print(isinstance(student, Czlowek))
    # print(isinstance(student, Zwierze))
    # print(isinstance(zwierze, Student))
    # print(issubclass(Student, Zwierze))

    print(zwierze.hello())
    print(czlowiek.hello())
    print(student.hello())

    # from collections import UserDict/UserList/Elipses - poczytac, pickle

    # praca domowa - kontunuacja addressbook
    # 1 lista slownik z walidacja
    # 2 obsluga plikow plus modulayzacja
    # 3 obiektowosc np
    # class DB: DB('baza.txt)
    # clss PErson: atybuty uzytkownikow
    # ma cos robic poza initem np __str__
    # obsluga wyjatkow