# Program: Exercicio6_8.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 14:20
# Updated:

number = int(input("Entre com um número para ser pesquisado na lista: "))
cont = 0
#bigger = len(lista)
contador = "NOK"
lista = list(range(1, 18))
while cont<len(lista):
    if (number == lista[cont]):
        print("Número %d encontrado, na posição %d."%(lista[cont], cont))
        contador = "Ok"
    if((cont==(len(lista)-1)) and (contador == "NOK")):
        print("Número não encontrado: %d" %number)
    cont+=1
