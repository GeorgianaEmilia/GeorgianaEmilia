# 1. Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
#  Un if else se explica prin punerea unei conditii care daca nu se indeplineste in if , intra in else , if else= daca nu, altceva

# 2.Verifica si afiseaza daca x este numar natural sau nu

# x >= 0  pass
# x < 0 fail
# x % 1 == 0  pass
# x % 1 != 0  fail

## x>=0 pass, x sa fie mai mare sau egal cu 0, deci sa fie nr natural, TRUE
# x= '2'
# if x.isdigit():
#     print('Este numar natural')
# else:
#     print('Nu este numar natural')
## x<0 fail x mai mic decat 0 numar negativ, deci FALSE
# x = '-2'
# if x.isdigit():
#     print('Este numar natural')
# else:
#     print('Nu este numar natural')
# # x%1!=0 fail (verifica daca restul impartirii lui x la 1 este diferit de 0=>TRUE => nu este numar natural , este float ) FALSE
# x = '2.3'
# if x.isdigit():
#     print('Este numar natural')
# else:
#     print('Nu este numar natural')
# # x % 1 == 0 pass restul impartit la 1 sa fie egal cu 0 deci numar natural, deci TRUE
# x = '2865487548'
# if x.isdigit():
#     print('Este numar natural')
# else:
#     print('Nu este numar natural')



# 3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

#1. x>0 Verificam ca numarul sa fie mai mare ca 0 si automat pozitiv, TRUE, pass
#2. x<0  Verificam ca numerele sa fie mai mici ca 0 deci negative, TRUE, pass
#3.x=0 0 e 0 neutru, TRUE, pass

# x=0
# if x>0:
#     print('Numarul este pozitiv!')
# elif x<0:
#     print('Numarul este negativ!')
# else:
#     print('Numarul este neutru!')



# 4. Verifica si afiseaza daca x este intre -2 si 13

#1. x>=-2
#2. x<=13

# x=14
# if x>=-2 and x<=13:
#     print('Numarul este intre -2 si 13!')


# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5


# x-y<5
# x=339898
# y=339
# if  (x-y)<5:
#     print(f'Diferenta dintre {x} si {y} este mai mica decat 5!')
# else:
#     print(f'Diferenta dintre {x} si {y} este mai mare decat 5!')
# 6.Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

# x>=27 fail pt ca folosind metoda not, ne schimba valoarea din true in false si invers
# x<=5 fail
# x<=27
# x<=5
# x=25
# if not(x<=27 and x>=5):
#     print('X nu este intre 5 si 27!')
# else:
#     print('X este intre 5 si 27!')
#
# x si y (int)
# 7.Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
#
# # 1. x==y
# # 2. x>y
# # 3. x<y
#
# x=input('Introdu un nr de la tastatura:')
# x=int(x)
# y=input('Introdu un nr de la tastatura:')
# y=int(y)
# if x==y:
#     print('X si Y sunt egale!')
# elif x>y:
#     print(f'X {x} este mai mare decat {y}!')
# else:
#     print(f'Y {y}  este mai mare decat {x}!')

# # 8.X, y, z - laturile unui triunghi
# # Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
#
# # x==y, y==z, x==z isoscel
# #  x==y==z echilateral
#
# x=input('Introdu un nr de la tastatura:')
# x=int(x)
# y=input('Introdu un nr de la tastatura:')
# y=int(y)
# z=input('Introdu un nr de la tastatura:')
# z=int(z)
#
# if x==y and y==z and x==z: #merge si x==y==z
#     print('Triunghiul este ECHILATERAL!')
# elif x==y or y==z or x==z:
#     print('Triunghiul este ISOSCEL!')
# else:
#     print('Triunghiul este unul oarecare!')


# 9.Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu
# a, e, i, o, u, ă, î (â)

# voc=input('Introdu o litera de la tastatura:')


# if voc=='a' or voc=='e' or voc=='i' or voc=='o' or voc=='u' or voc=='ă' or voc=='î' or voc =='â':
#     print(f'Litera " {voc} "este o vocala!')
# else:
#     print('Litera nu este vocala')
# voc=input('Introdu o litera de la tastatura:')
# vocala='aeiouăîâ'
# voc=voc.lower()
# if voc in vocala:
#     print('Litera este vocala')
# else:
#     print('Litera nu este vocala')
# 10.
# Transforma si printeaza notele din sistem romanesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
#
# x=input('Introdu de la tastatura nota: ')
# x=float(x)
# if   x >= 9:
#     x='A'
# elif x >= 8:
#     x='B'
# elif x >= 7:
#     x='C'
# elif x >= 6:
#     x='D'
# elif x >  4:
#     x='E'
# elif x <= 4:
#     x='F'
#
# print(f'Ai primit nota {x} !')
# # 11.
# 11. Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
# x=input('Introdu de la tastatura un numar: ')
# if len(x) >=4:
#     print('Numarul are minim 4 cifre!')
# else:
#     print('Numarul nu are minim 4 cifre !')
# a 2a varianta de rezolvare

# x=70564
# if x>=1000:
#     print('Numarul are minim 4 cifre!')

# 12.Verifica daca x are exact 6 cifre
#  x==6

# x=input('Introdu un numar ')
#
# if len(x)==6:
#     print('Numarul are exact 6 cifre!')
# else:
#     print('Numarul nu are 6 cifre!')
# x=345678
# if x>=100000 and x<1000000:
#     print("Numarul are exact 6 cifre !")


#13. Verifica daca x este numar par sau impar
# x=579
# if x%2==0:
#     print('Numarul este par!')
# else:
#     print('Numarul este impar!')
#

# x, y, z (int)
#14. Afiseaza care este cel mai mare dintre ele?
#
# x=2
# y=4
# z=4
# if x>=y and x>=z:
#     print(f'{x} este cel mai mare numar !')
# elif y>=x and y>=z:
#     print(f'{y} este cel mai mare numar !')
# elif z>=x and z>=y:
#     print(f'{z} este cel mai mare numar !')

# 15.
# X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu

# x=40
# y=70
# z=70
# if x+y+z==180 and x>0 and y>0 and z>0:
#     print('Triunghiul este valid !')
# else:
#     print('Triunghiul nu este valid!')

#robotel telefonic

 # LISTE
 #