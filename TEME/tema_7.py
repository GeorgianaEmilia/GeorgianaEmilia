'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura

ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata

Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte

POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’

Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui

'''

# ABSTRACTION
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(self):
        print('Cel mai probabil am colturi!')


# INHERITANCE
class Patrat(FormaGeometrica):
    __latura = None

    # ENCAPSULATION
    def get_latura(self):  # folosim sa afisam latura
        return self.__latura

    def set_latura(self, latura_dorita):  # folosim setter ca sa setam o alta latura
        self.__latura = latura_dorita

    def delete_latura(self):
        self.__latura = None

    def aria(self):
        print(f'Aria patratului este {self.__latura * self.__latura} !')


class Cerc(FormaGeometrica):
    __raza = None

    def get_raza(self):  # folosim sa afisam raza
        return self.__raza

    def set_raza(self, raza_dorita):  # folosim setter ca sa setam o alta raza
        self.__raza = raza_dorita

    def delete_raza(self):
        self.__raza = None

    def aria(self):
        print(f'Aria cercului este: {(self.__raza * self.__raza) * self.pi}!')

    def descrie(self):
        print('Eu nu am colturi!')

p=Patrat()
p.set_latura(10)
p.aria()
print(p.get_latura())
print(p.delete_latura())
p.descrie()
p.set_latura(5)

c=Cerc()
c.set_raza(4)
c.aria()
c.descrie()

i=Patrat()
i.set_latura(240)
i.descrie()
i.aria()
print(i.get_latura())

print(p.get_latura()*c.get_raza()*i.get_latura())
