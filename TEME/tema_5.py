import datetime
#from datetime import datetime
from collections import Counter
#1. Functie care sa calculeze si sa returneze suma a 2 numere
# def suma_numere(nr1,nr2):
#     return nr1+nr2
# x=suma_numere(45,56)
# print(f'Suma a 2 numere este {x} !')

#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
# nr=int(input('Introduceti un numar: '))
# def numar_parsauimpar(nr):
#     if nr %2==0:
#         return True
#     else:
#         return False
# print(f'Numarul introdus de la tastatura este {numar_parsauimpar(nr)}')
#3. Functie care returneaza numarul total de caractere din numele tau complet.
#(nume, prenume, nume_mijlociu)

# def numartotal_nume(nume, prenume, nume_mijlociu):
#     return len(nume)+len(prenume)+len(nume_mijlociu)
# x=numartotal_nume('Ciontic','Georgiana','Emilia')
# print(f'Numele tau complet are {x} caractere!')

#4. Functie care returneaza aria dreptunghiului
# def aria_dreptunghiului(L,l):
#     return L*l
# x=aria_dreptunghiului(5,6)
# print(x)
#5. Functie care returneaza aria cercului
# def aria_cercului( raza):
#     return 3.14*(raza*raza)
# x=aria_cercului(3)
# print(x)

#6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

# def caracter_x(caracter,cuvant):
#     if caracter in cuvant:
#         return True
#     else:
#         return False
# x=caracter_x('r','sesiune')
# print(x)

#7. Functie fara return, primeste un string si printeaza pe ecran:
#⦁	Nr de caractere lower case este x
#⦁	Nr de caractere upper case exte y

# def abc(cuvant):
#     liter_mare=0
#     litera_mica=0
#     for litera_din_cuvant in cuvant:
#         if litera_din_cuvant.isupper():
#             liter_mare+=1
#         else:
#             litera_mica+=1
#     print(f'Nr de caractere upper case este {liter_mare} !')
#     print(f'Nr de caractere lower case este {litera_mica} !')
#
# x=input('Introduceti un string de la tastatura: ')
# abc(x)

#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
# b=[2,3,4,-3,-867548,-45,-45.789, 23.5,765.0]
#
# def lista_nr(lista):
#     lista_nrpozitive=[]
#     for a in lista:
#         if a > 0:
#             lista_nrpozitive.append(a)
#     return lista_nrpozitive
#
# raspuns=lista_nr(b)
# print(f'Numerele pozitive din lista sunt: {raspuns}!')

# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# ⦁	Primul numar x este mai mare decat al doilea nr y
# ⦁	Al doilea nr y este mai mare decat primul nr x
# ⦁	Numerele sunt egale.
# x=input('Introduceti un numar de la tastatura: ')
# y=input('Introduceti un numar de la tastatura: ')
#
# def numere(nr1, nr2):
#     if nr1>nr2:
#         print('Primul nr mai mare decat al doilea numar')
#     elif nr2 > nr1:
#         print('Al doilea nr y este mai mare decat primul nr')
#     else:
#         print('Numerele sunt egale')
# numere(x,y)

#10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

# set_numere={1,2,3,4,5,6,7,8}
# def functie_numar(n1,numere):
#     if n1 in numere:
#         print('Nu am adaugat numarul in set. Acesta exista deja')
#         return False
#     else:
#         numere.add(n1)
#         print('Am adaugat numarul nou in set!')
#         return True
#
#
# functie_numar(4,set_numere)
# print(set_numere)

# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna .


# def zile_luna(luna):
#     luni_28 = ['Februarie']
#     luni_30 = ['Aprilie', 'Iunie', 'Septembrie', 'Noiembrie']
#     luni_31 = ['Ianuarie', 'Martie', 'Mai', 'Iulie', 'August', 'Octombrie', 'Decembrie']
#     if luna in luni_28:
#         return 28
#     elif luna in luni_30:
#         return 30
#     elif luna in luni_31:
#         return 31
#
# lunatastatura=input('Luna : ')
# print(zile_luna(lunatastatura))

#12. Functie calculator care sa returneze 4 valori
#Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

# def calculator(n1,n2):
#     return n1+n2,n1-n2,n1*n2, n1/n2
#
# a,b,c,d=calculator(200,20)
# print(f'Suma: {a} ')
# print(f'Diferenta: {b} ')
# print(f'Inmultirea: {c} ')
# print(f'Impartirea: {d} ')

#13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare litera
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
#
# def lista_cifre(cifre):
#     my_dict={}
#     for i in range(0,10):
#         my_dict[i]=cifre.count(i)
#     return my_dict
# lista=[1, 3, 1, 5, 9, 7, 7, 5, 5]
# print(lista_cifre(lista))

#14. Functie care primeste 3 numere
#Returneaza valoarea maxima dintre ele

# def valoarea_maxima(nr1,nr2,nr3):
#     if nr1>nr2 and nr1>nr3:
#         return nr1
#     if nr2>nr1 and nr2>nr3:
#         return nr2
#     if nr3>nr1 and nr3>nr2:
#         return nr3
#
# raspuns=valoarea_maxima(3243432,567,676763)
# print(f'Valoarea maxima este {raspuns} !')

#15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)

# def suma_nr(nr):
#     sum=0
#     for i in range(0,nr+1):
#         sum+=i
#     return sum
# x=suma_nr(3)
# print(f'Suma tuturor numerelor este: {x} !')

# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
# nume = input('Introduceti un nume de la tastatura: ')
# exceptii_fete = ['carmen','erin', 'zoe','iris','ingrid',]
# exceptii_baieti = ['mihnea', 'mircea', 'horia', 'horea','nita','aldea','luca']
#
#
# def gen(numemetoda):
#     if numemetoda in exceptii_fete:
#         print('Este fata!')
#     elif numemetoda in exceptii_baieti:
#         print('Este baiat!')
#     elif numemetoda[len(numemetoda)-1] =='a':
#         print('Este fata!')
#     else:
#         print('Este baiat!')
#
# gen(nume.lower())


# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}

# lista1=[1,1,2,3,-2,-975.975,876.9]
# lista2=[2,2,3,4,4,4,4,5,6,7,8,9,0,45,678,343,321,5645,-1,-2,-975.975,876.9]
# listanoua=[]
# def primeste_liste(list1,list2):
#    return (set(list1).intersection(list2))
#
# print(primeste_liste(lista1,lista2))


#18. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida

# def aplicare_discount(pret,reducere):
#     if reducere > 100:
#         return 'Reducere invalida'
#     else:
#      pretdupareducere=pret-(pret*(reducere/100))
#      return pretdupareducere
# x = aplicare_discount(100,10)
# print(f'Pretul dupa reducere este: {x} !')

#19. Functie care sa afiseze data si ora curenta
#
# def data_ora():
#     return datetime.today()
#
# print(data_ora())


#20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

def get_birthday():
    today = datetime.date.today()
    future_bday=datetime.date(2023,2,21)
    return (future_bday-today).days
print(f"Remains {get_birthday()} days until my bday !")


