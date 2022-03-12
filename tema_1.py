#TODO TEMA 1 INCEPE DE AICI!!
# 1.
#Variabila= pentru a lucra cu date trebuie sa declaram zone de memorie (variabile)
#Variabila=o cutiuta din memorie in care stocam valori, aceasta este creata in momentul in care ii atribuim o valoare
#variabila= are un nume unic pentru a fi identificata ulterior si folosita
#variabila=nu putem pune spatiu in numele variabilei (my_var snake case care este de preferat sa fie folosit in Python , MyVar camel case)

# 2.
# marcaMasina= 'Ford'    #string
# nrKm= 10000            #int
# pret_masina= 4000.45   #float
# asigurare=True         #bool
#
# print(type(pret_masina))
# print(round(pret_masina))
# pret_masina=4000
# print(type(pret_masina))
# print('Vreau sa cumpar o masina marca ' + marcaMasina + ' !' )
# print(f'Masina pe care vreau sa o cumpar are {nrKm} KM!')
# print(f'{marcaMasina} are pretul de {pret_masina} €!')
# print(f'Masina pe care urmeaza sa o achizitionez {marcaMasina} cu {nrKm} Km la pretul de {pret_masina} are asigurare? ' + f'{asigurare}' )

# nume=input('Alege un nume: ')
# prenume=input('Introdu prenumele tau: ')
# print(f'Numele complet are {len(nume+prenume)} caractere!')


# lungime=input('Adauga lungimea dreptunghiului ')
# lungime=int(lungime)
# latime=input('Adauga latimea dreptunghiului')
# latime=int(latime)
# print(f'Aria dreptunghiului este {(lungime*latime)} !')
#acelasi string
#declara un string nou care sa fie format din primele 5 caractere + ultimele 5

# tema= 'Coral is either the stupidest animal or the smartest rock'
# last_index=len(tema)
# print(last_index)
# # nrCaractere=input('Introdu numarul de caractere')
#  nrCaractere=int(nrCaractere)
#  temafinala=last_index-nrCaractere
# temanoua= tema[0:5]+tema[last_index-5:last_index]
# print(temanoua)
#
# tema= 'Coral is either the stupidest animal or the smartest rock'
# print(tema.replace('the', 'THE'))


# tema= 'Coral is either the stupidest animal or the smartest rock'
# temanoua= tema.index('rock')
# print(temanoua)
# print(tema[0:temanoua])\


# diverse= input('Introdu cuvantul: ')
# diverse_index= len(diverse)-1
# print(diverse[0] + diverse[diverse_index])
# assert diverse[0].upper() == diverse[diverse_index].upper()
# print('Primul si ultimul caracter sunt la fel')

# casa='0123456789'
# last_index= len(casa)
# print(casa[0:last_index:2])
# print(casa[1:last_index:2])

# tema='Coral is either the stupidest animal or the smartest rock'
# assert tema.isnumeric()

# numar=input('Introdu cuvantul:')
# last_index=len(numar)-1
# numarimpar= last_index/2
# numarimpar=int(numarimpar)
# print(numar[numarimpar])

# diverse=input('Introdu un cuvant')
# assert diverse == diverse[::-1]
# print('Este palindrom')


# nume, varsta =input('scrie aici nume si varsta ').split()
# print(nume+ varsta)
# citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incear
# ca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla
#citeste ceva de la tastatura
# problema=input('Scrie aici ceva')
# #salveaza primul caracter intr-o variabila  care este pe pozitia [0]
# primulCaracter=problema[0]
# #vedem cate caractere avem -1, len incepe de la 1, index de la 0
# last_index=len(problema)-1
# #facem un str nou in care declaram primul str 'problema', [1:last_index]->excludem primul si
# # ultimul caracter apoi inlocuim primul caracter cu primul caracter cu upper case pt a ne inlocui primul caracter care poate se regaseste
# # in toata PROBLEMA cu upper cu exceptia primului si a ultimului caracter
# problFinala=problema[1:last_index].replace(primulCaracter,primulCaracter.upper())
# problFinala=problema[0] + problFinala + problema[last_index]
# print(problFinala)

# citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****

nume=input('user:')
parola=input('pass')
steluta= '*'*len(parola)
print(f'Parola pt user {nume} este {steluta} si are {len(parola)} caractere!!!!')

