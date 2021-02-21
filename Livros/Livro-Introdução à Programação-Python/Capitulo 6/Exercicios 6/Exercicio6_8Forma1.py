# Program: Exercicio6_8.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 21:17
# Updated:

lista = [3,7,1,8,5,10]
cont = 0
number = int(input("Entre com um número que será pesquisado: "))
for e in lista:
    if e == number:
        print("%d encontrado no posição %d" %(number, cont))
        break
    cont+=1
else:
    print("Número não encontrado!")
