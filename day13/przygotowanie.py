#
# try:
#     with open("dane.csv","r+") as sprawdzamy_plik:
#         line=sprawdzamy_plik.readline()
#         print("to jest kod bez bledu w try")
# except FileNotFoundError:
#     print("nie ma pliku")
# except IOError:
#     print("nie mozna przeczytac linijki")
# finally:

class Samochod:
    def __init__(self,marka,kolor):
        self.marka=marka
        self.kolor=kolor

auto1=Samochod("volvo","czarny")
print(auto1.model)