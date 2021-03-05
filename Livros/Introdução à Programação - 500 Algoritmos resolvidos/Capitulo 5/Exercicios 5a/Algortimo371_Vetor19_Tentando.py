# Program: Algortimo371_Vetor19_Tentando.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/05/2020 - 20:19
# Updated: 04/05/2020 - 21:32 

#------------Excrevi a essa parte do programa para -------------#
#------------saber o que eu devo fazer no resto ----------------#
#lista = list(range(10))
#cont  = 0
#cont2 = 0
#while cont<len(lista):
#    test = lista[cont]
#   if (test == 7):
#       del lista[cont]
#       cont2+=1
#   if (test == 3):
#       del lista[cont]
#       cont2+=1
#   print(lista[cont])
#   cont+=1
#print("\n\n")
#print(cont2)
#print("\n\n")

#--------------------------------------------------------------#
#--------------------------------------------------------------#

quantity1 = 5
quantity2 = 6
lista1 = list()
lista2 = list()
#--------Primeira parte do programa: Preencher as listas-------#
for e in range(quantity1):
    number =  int(input("Enter with the %d° number: " %(e+1)))
    lista1.append(number)
print("\n")
for n in range(quantity2):
    number =  int(input("Enter with the %d° number: " %(n+1)))
    lista2.append(number)
print("\n")
#--------Seunga partede programa: Veririficar se em cada lista-#
#--------Algum número se repete internamente-------------------#
cont = 0
while (cont<len(lista1)):
    test = 0
    cont2 = 0
    while cont2<len(lista1):
        if lista1[cont] == lista1[cont2]:
            test+=1
        cont2+=1
    if test >= 2:
        del lista1[cont]
    print(lista1[cont], end=" ")
    cont+=1
cont = 0

print("\n")
while (cont<len(lista2)):
    test = 0
    cont2 = 0
    while cont2<len(lista2):
        if lista2[cont] == lista2[cont2]:
            test+=1
        cont2+=1
    if test >= 2:
        del lista2[cont]
    print(lista2[cont], end=" ")
    cont+=1   
print("\n\n")

#--------Vamos agora verificar o que há de diferente nas -----#
#--------duas lista e por em uma terceira lista --------------#

lista3 = lista1[:]+lista2[:]
lista4 = list()
print()
print(lista3)
print()
cont = 0
dels = 0
cont4 = 0
while (cont<len(lista3)):
    test = 0
    cont2 = 0
    while cont2<len(lista3):
        if lista3[cont] == lista3[cont2]:
            test+=1
        cont2+=1
    if test >= 2:
        dels+=1
    else:
        lista4.append(lista3[cont])
        print(lista4[cont4], end=" ")
        cont4+=1
    cont+=1
cont = 0



    

