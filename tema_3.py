# # 1.Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# # Afiseaz-o
# # Afiseaz-o in ordine inversa folosind slicing
# # Cautati o metoda care face acelasi lucru
# # Folositi metoda
# # Printati lista
# # Observati ca aceasta metoda va salva modificarile
#
# note_muzicale= ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# #afisare lista
# print(note_muzicale)
# # afisare inversa
# print(note_muzicale[::-1])
# #o alta metoda de a afisa in ordine inversa lista
# #metoda reverse
# note_muzicale.reverse() # aici cand nu intelegeam !intrebare, de ce daca pun metoda asta direct in print imi afiseaza NONE, dar daca o las asa si dau print pe alta linie de cod functioneaza?
# # reverse functioneaza pe lista initiala acesta fiind "independent" , vom observa ca el si-a facut treaba cand printam lista pe care am aplicat metoda reverse
# #printez lista
# print(note_muzicale)
# #a doua metoda
# #am permanentizat lista inversata temporar prin slicing in lista initiala
# note_muzicale =note_muzicale[::-1]
#  print(note_muzicale) #aici imi afiseaza ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do'] pt ca mai sus avem reverse care a salvat modificarile, iar acum am afisat lista inversata in urma reverse ului


# lista1=['a','b','c','d','e']
# print(lista1[::-1])
# lista1=lista1[::-1]
# print(lista1)
#
# lista1.reverse()
# print(lista1)



# # 2. De cate ori apare ‘do’?
# print(note_muzicale.count('do'))

# 3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
# Afisati lista ordonata astfel [0,1,2,3,4,5,6] intr-o singura lista

# list1=[3,1,0,2]
# list2=[6,5,4]
# list1.extend(list2)
# print(list1)
# list1.append(list2[0])
# list1.append(list2[1])
# list1.append(list2[2])
# print(list1)
# list1.sort()
# print(list1)


# 4. Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista

# list1=[3,1,0,2]
# list2=[6,5,4]
# list1.extend(list2)
# print(list1)
# list1.sort()
# print(list1)
# list1.remove(0)
# print(list1)

# 5. Folosind un if verificati lista generata la ex3 si afisati
# ⦁	Lista este goala
# ⦁	Lista nu este goala

# list1=[3,1,0,2]
# list2=[6,5,4]
# list1.extend(list2)
# print(list1)
# list1.sort()
# print(list1)
# list1.remove(0)
# print(list1)
# list1.clear()
# print(list1)

# if len(list1) == 0: #al doilea caz in care testam listele goale
#     print('Lista este goala!')
# else:
#     print('Lista nu este goala!') #primul caz in care testam ca lista nu este goala

# 6.Folositi o functie care sa stearga lista de la ex3

# list1=[3,1,0,2]
# list2=[6,5,4]
# # list1.extend(list2)
# # print(list1)
# list1.append(list2[0])
# list1.append(list2[1])
# list1.append(list2[2])
# print(list1)
# list1.sort()
# print(list1)
# list1.clear()
# print(list1)


# 7. Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala
# list1=[3,1,0,2]
# list2=[6,5,4]
# list1.extend(list2)
# print(list1)
# list1.sort()
# print(list1)
# list1.remove(0)
# print(list1)
# list1.clear()
# print(list1)
#
# if len(list1) == 0: #al doilea caz in care testam listele goale
#     print('Lista este goala!')
# else:
#     print('Lista nu este goala!') #primul caz in care testam ca lista nu este goala

#  8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

# dict1= {'Ana ': 8, 'Gigel': 10, 'Dorel': 5}
#
# print(dict1.keys())

# 9. Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota x’
# X il veti lua programatic folosind o functie
#
# dict1= {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
#
# print(f'Ana a luat nota {dict1.get("Ana")}')

# print(dict1.get('Ana'))
# print(dict1['Ana'])
# nume=list(dict1.keys())[0]
# print(list(nume)[0])


# print(f'{list(dict1.keys()) [list(dict1.values()).index(5)]} a luat nota  {dict1.get("Dorel")} !')
# list(dict1.keys()) -> imi afiseaza toate keys urile din dictionar
#apoi avem list(dict1.values()).index(8) lista dictionarului din care extragem toate valorile keys urilor si in functie de index aflam cheia


# 10. Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare

# dict1= {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# dict1['Dorel']= '6'
# print(dict1)

#  11. Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi

# dict1= {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# dict1.pop('Gigel')
# dict1['Ionica']= 9
# print(dict1)

#  12. Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

# zile_sapt={'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend={'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)

# 13. Folositi un if si verificati daca
# ⦁	Weekend este un subset al zilelor din sapt
# ⦁	Weekend nu este un subset al zilelor din sapt

# zile_sapt={'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend={'sambata', 'duminica'}
#
# if weekend.issubset(zile_sapt):
#  print('Weekend este un subset al zilelor din sapt')
# else:
#     print('Weekend nu este un subset al zilelor din sapt')

#  14.Afisati diferentele dintre aceste 2 seturi

# zile_sapt={'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend={'sambata', 'duminica'}
#
# print(zile_sapt.difference(weekend))

# 15. Afisati intersectia elementelor din aceste 2 seturi
# zile_sapt={'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend={'sambata', 'duminica'}
# print(zile_sapt.intersection(weekend))

#  16. Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# ⦁	Efectuam schimbarea
# ⦁	Stergem jucatorul scos din lista
# ⦁	Adaugam jucatorul intrat
# ⦁	Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# ⦁	Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# ⦁	Afisati ‘mai aveti z schimbari’
# Testati codul cu diferite valori

# jucatori= ['Cristi', 'George', 'Adrian', 'Cosmin', 'Andrei']
# juca_lista= input('Introduceti un jucator: ')
# schimbari_efectuate= 0
# #
# if juca_lista in jucatori and schimbari_efectuate > 0:
#     jucatori.remove(juca_lista)
#     jucatori_noi=input('Introduceti de la tastatura numele noului jucator: ')
#     jucatori.append(jucatori_noi)
#     schimbari_efectuate=schimbari_efectuate-1
#     print(f'A intrat {jucatori_noi} si a iesit {juca_lista}, mai aveti {schimbari_efectuate} schimbari !')
# else:
#     print(f'Nu se poate efectua schimbarea, deoarece jucatarul {jucatori} nu e in teren!')
#     print(f'Mai aveti {schimbari_efectuate} schimbari !')

