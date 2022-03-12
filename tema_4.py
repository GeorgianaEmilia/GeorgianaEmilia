from random import randint

''' 1.Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # iteram cu un for si afisam 'Masina mea preferata este x'
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]} !')
# # iteram cu un for each
# for masina in masini:
#     print(f'Masina mea preferata este {masina} !') # am pus {masina} pentru ca for each ne ia strict fiecare element in parte
# # iteram acum lista cu un while
# x=0
# while x < len(masini):
#     print(f'Masina mea preferata este {masini[x]} !')
#     x += 1
#
'''2.
Aceeasi lista
Folositi un for else
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
In else 
   Printati lista
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(1,len(masini)-1):
#       masini[i]=masini[i].upper()
# else:
#     print(f'Masina mea preferata este {masini} !')
'''3. 
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin modalitatea aleasa de voi
Daca masina e mercedes 
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if i == masini.index('Mercedes'):
#         print(f'Am gasit masina dorita de dvs {masini[i]} !')
#         break
#     else:
#         print(f'Am gasit masina {masini[i]} .Mai cautam')

'''Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
Iterati prin lista

Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
(nu trebuie else)
Printati S-ar putea sa va placa masina x
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#         continue
#     print(f'S-ar putea sa va placa {masini[i]} !')
'''5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
⦁	Salvati aceste masini in masini_vechi
⦁	Suprascrieti-le cu ‘Tesla’
Printati Modele vechi: x
Modele noi: x
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi= []
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#        masini_vechi.append(masini[i])
#        masini[i]='Tesla'
# print(f'Modele vechi {masini_vechi}')
# print(f'Modele noi {masini} !')

'''6. 
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
'''
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# client= 15000
# for masini,pret in pret_masini.items():
#     if pret < client:
#      print(f'Pentru un buget de sub 15000 euro puteti alege masina {masini} !')

'''7.
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# z=0
# for i in range(len(numere)):
#     if numere[i] == 3:
#         z+=1
# print(f'Numarul 3 apare de {z} .')

'''8. 
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# total=0
# for numar in numere:
#     total +=numar
# print(f'Suma {total} .')

'''9. 
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x=0
# for numar in numere:
#     if numar > x:
#      x = numar
# print(f'Cel mai mare numar este {x} !')

'''
10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# for numar in numere:
#     if numar > 0:
#         print(-abs(numar))

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# for numar in numere:
#     if numar > 0:
#         print(numar*(-1))

'''11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere 
Populati corect celelalte liste
Afisati cele 4 liste la final
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for alt_numar in alte_numere:
#     if alt_numar % 2 == 0:
#         numere_pare.append(alt_numar)
#     if alt_numar % 2 != 0:
#         numere_impare.append(alt_numar)
#     if alt_numar > 0:
#         numere_pozitive.append(alt_numar)
#     if alt_numar < 0:
#         numere_negative.append(alt_numar)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)
'''
12.
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# x=len(alte_numere)
# for i in range(x):

'''13.
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
⦁	Nr secret e mai mare
⦁	Nr secret e mai mic
⦁	Felicitari! Ai ghicit!
'''

# numar_secret = randint(1,30)
# Numar_ghicit = None
# print(numar_secret)
# while True:
#     nr_user=input('Numar ales de tine: ')
#     nr_user=int(nr_user)
#     if numar_secret > nr_user:
#         print('Numarul secret e mai mare')
#     elif numar_secret < nr_user:
#         print(' Numarul secret e mai mic !')
#     elif numar_secret == nr_user:
#         print('Felicitari ai ghicit !')
#         Numar_ghicit=nr_user
#         break
# print(f'Numarul ghicit este {Numar_ghicit} !')
'''Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777
'''
# alege_numar=input('Alege un numar: ')
# alege_numar=int(alege_numar)
# for i in range(alege_numar+1):
#         print(str(i)* i)

'''15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
'''

# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for i in range(len(tastatura_telefon)):
#   for y in range(len(tastatura_telefon[i])):
#     print(f'Cifra curenta este {tastatura_telefon[i][y]} !')
