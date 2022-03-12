from datetime import date
from tabulate import tabulate

'''
1.
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''
# class Cerc:
#
#     def __init__(self,raza,culoare):
#         self.raza=raza
#         self.culoare=culoare
#
#     def descrie_cerc(self):
#         print(f'Culoarea este {self.culoare}!')
#         print(f'Raza este {self.raza}!')
#
#     def aria(self):
#         return 3.14*(self.raza*self.raza)
#
#     def diametru(self):
#         return 2*self.raza
#
#     def circumferinta(self):
#         return 3.14*2*self.raza
#
# cerc1=Cerc(2,'alb')
# cerc1.descrie_cerc()
# print(f'Aria cercului este: {cerc1.aria()}!')
# print(f'Diametrul cercului este: {cerc1.diametru()}!')
# print(f'Circumferinta cercului este: {cerc1.circumferinta()}!')

'''Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param 
o noua culoare si va suprascrie atributul self.culoare. 
Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''

# class Dreptunghi:
#     lungime=None
#     latime=None
#     culoare='alb'
#
#     def __init__(self,lungime,latime,culoare):
#         self.lungime=lungime
#         self.latime=latime
#         self.culoare=culoare
#
#     def descrie_dreptunghi(self):
#         print(f'Lungimea este {self.lungime}!')
#         print(f'Latimea este {self.latime}!')
#         print(f'Culoarea este {self.culoare}!')
#
#     def aria(self):
#         return self.lungime * self.latime
#
#     def perimetru(self):
#         return 2*(self.lungime+self.latime)
#
#     def schimba_culoarea(self):
#         self.culoare='albastru'
#
# dreptunghi1=Dreptunghi(10,4,'alb')
# dreptunghi1.culoare='albastru'
# dreptunghi1.descrie_dreptunghi()
# print(f'Aria dreptunghiului este: {dreptunghi1.aria()}')
# print(f'Perimetrul dreptunghiului este: {dreptunghi1.perimetru()}')
# dreptunghi2=Dreptunghi(25,5,'alb')
# print(f'Aria dreptunghiului este: {dreptunghi2.aria()}')
# print(f'Perimetrul dreptunghiului este: {dreptunghi2.perimetru()}')

'''3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''


# class Angajat:
#     nume = None
#     prenume = None
#     salariu = None
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'Numele anagajatului este {self.nume} !')
#         print(f'Prenumele anagajatului este {self.prenume} !')
#         print(f'Salariul anagajatului este {self.salariu} !')
#
#     def nume_complet(self):
#         return self.nume + ' ' + self.prenume
#
#     def salariu_lunar(self):
#         return self.salariu
#
#     def salariu_anual(self):
#         return 12 * self.salariu
#
#     def marire_salariu(self, marire):
#         return self.salariu + (marire / 100 * self.salariu)
#
#
# ionel = Angajat('Sorescu', 'Ionel', 5000)
# ionel.descrie()
# print(f'Numele complet este: {ionel.nume_complet()}!')
# print(f'Salariul lunar al angajatului {ionel.nume_complet()} este de {ionel.salariu_lunar()} LEI !')
# print(f'Salariul anual al angajatului {ionel.nume_complet()} este de {ionel.salariu_anual()} LEI !')
# print(f'Salariul angajatului {ionel.nume_complet()} dupa marirea cu 15% este {ionel.marire_salariu(15)}!')
#
# ciprian=Angajat('Condu', 'Ciprian',10000)
# ciprian.descrie()
# print(f'Numele complet este: {ciprian.nume_complet()}!')
# print(f'Salariul lunar al angajatului {ciprian.nume_complet()} este de {ciprian.salariu_lunar()} LEI !')
# print(f'Salariul anual al angajatului {ciprian.nume_complet()} este de {ciprian.salariu_anual()} LEI !')
# print(f'Salariul angajatului {ciprian.nume_complet()} dupa marirea cu 10% este {ciprian.marire_salariu(10)}!')


'''4.
Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total 
Telefon |      7       |       700       | 49000     
'''


# class Factura:
#     seria = 123456
#     numar = None
#     nume_produs = None
#     cantitate = None
#     pret_buc = None
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self,cantitate_noua):
#         self.cantitate = cantitate_noua
#
#     def schimba_pretul(self):
#         self.pret_buc = 1500
#
#     def schimba_nume_produs(self,produs_nou):
#         self.nume_produs = produs_nou
#
#     def calc_total(self):
#         return self.pret_buc * self.cantitate
#
#     def genereaza_factura(self):
#         print(tabulate([[self.seria,self.nume_produs, self.cantitate, self.pret_buc, self.calc_total(), date.today()]],
#                        headers=['Serie Factura','Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))
#
#
# factura1 = Factura(799432198, 'Telefon', 10, 1000)
# factura1.genereaza_factura()
# factura1.schimba_cantitatea(20)
# factura1.schimba_pretul()
# factura1.schimba_nume_produs('Iphone')
# factura1.genereaza_factura()
# factura2 = Factura(798532459, 'Laptop', 5, 3500)
# factura2.genereaza_factura()
# factura2.schimba_cantitatea(15)
# factura2.genereaza_factura()
# factura3 = Factura(757638321, 'Tastatura', 20, 100)
# factura3.genereaza_factura()
# factura4 = Factura(753454564, 'Boxe', 50, 300)
# factura4.genereaza_factura()

'''
5. 
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

# class Cont:
#
#     def __init__(self,iban,titular_cont,sold):
#         self.iban=iban
#         self.titular_cont=titular_cont
#         self.sold=sold
#
#     def descriere(self):
#         print(f'IBAN-ul dumneavoastra este: {self.iban} !')
#         print(f'Titularul de cont este: {self.titular_cont} !')
#         print(f'Aveti urmatorul sold: {self.sold} !')
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} !')
#
#     def debitare_cont(self):
#         amount_debitare = float(input("Introduceti suma pe care vreti sa o transferati:  "))
#         if amount_debitare > self.sold:
#          print('Nu mai aveti fonduri disponibile')
#         else:
#            self.sold -= amount_debitare
#            print(f'Mai aveti un sold de {self.sold}')
#
#     def creditare_cont(self):
#         amount_creditare = float(input("Introduceti suma pe care ati primit-o:  "))
#         self.sold += amount_creditare
#         print(f'Contul a fost alimentat cu: {self.sold}')
#
# cont1=Cont(9874646224544,'Ion Ion', 7800)
# cont1.descriere()
# cont1.afisare_sold()
# cont1.debitare_cont()
# cont1.creditare_cont()

'''6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''

class Masina:
    marca= 'Dacia'
    model=None
    viteza_maxima=230
    viteza_actuala=0
    culoare='gri'
    culori_disponibile=['rosu','verde','alb','albastru','portocaliu','negru','galben']
    inmatriculata=False

    def __init__(self,model,viteza_maxima):
        self.model=model
        self.viteza_maxima=viteza_maxima

    def descrie(self):
        print(f'Marca masinii este: {self.marca}!')
        print(f'Modelul masinii este: {self.model}!')
        print(f'Viteza maxima a masinii este: {self.viteza_maxima}!')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}!')
        print(f'Culoarea masinii este: {self.culoare}!')
        print(f'Masina este inamtriculata: {self.inmatriculata}!')

    def inmatriculare(self):
        self.inmatriculata= True
        return self.inmatriculata

    def vopseste_masina(self,noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare = noua_culoare
            print(f'Noua culoare a masinii este: {self.culoare}!')
        else:
            print('Culoarea aleasa de dvs nu este in paletarul nostru!')

    def accelereaza(self,viteza_noua):
        self.viteza_actuala=viteza_noua
        if self.viteza_actuala < 0:
            print('EROARE!')
        elif self.viteza_actuala >= self.viteza_maxima:
            print(f'Viteza maxima este: {self.viteza_maxima}!')
        else:
            print(f'Viteza actuala este: {self.viteza_actuala}!')

    def franeaza(self,viteza_noua):
        self.viteza_actuala=viteza_noua
        if self.viteza_actuala ==0:
            print('Masina s-a oprit!')
        else:
            print('Masina nu s-a oprit!')

masina1=Masina('Logan',230)
masina1.descrie()
print(f'Masina a fost inmatriculata: {masina1.inmatriculare()}!')
masina1.vopseste_masina('bej')
masina1.vopseste_masina('rosu')
masina1.accelereaza(-34)
masina1.accelereaza(0)
masina1.accelereaza(10)
masina1.accelereaza(231)
masina1.franeaza(0)
masina1.franeaza(4)

'''7. Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task() - se va adauga in dict
finalizeaza_task() - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare

daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.

Daca acesta raspunde nu - la revedere

daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

'''
#
# class ToDoList:
#     dict={}
#
#     def adauga_task(self,nume_task,descriere_task):
#         self.dict[nume_task]=descriere_task
#
#     def finalizeaza_task(self,nume_task):
#         del self.dict[nume_task]
#
#     def afiseaza_todo_list(self):
#         print(f'Task-urile din TODO sunt: {self.dict.keys()}')
#
#     def afiseaza_detalii_suplimentare(self,nume_task):
#         if nume_task in self.dict:
#          print(f'Descrierea task-ului: {nume_task} si detaliile suplimentare {self.dict[nume_task]} !')
#         else:
#             raspuns=input('Vrei sa adaugi task ul in lista? : ')
#             if raspuns == 'DA':
#                 descriere_task=input('Introdu descrierea pentru noul task: ')
#                 self.dict[nume_task]=descriere_task
#                 print(f'Descrierea task-ului: {nume_task} si detaliile suplimentare {self.dict[nume_task]} !')
#             else:
#                 print('La revedere!')
#
# todolist1=ToDoList()
# todolist1.adauga_task('Cumparaturi','Cumparam fructe,paine,apa')
# todolist1.afiseaza_todo_list()
# todolist1.afiseaza_detalii_suplimentare('Cumparaturi')
# todolist1.afiseaza_detalii_suplimentare('Masini')
# todolist1.afiseaza_todo_list()








