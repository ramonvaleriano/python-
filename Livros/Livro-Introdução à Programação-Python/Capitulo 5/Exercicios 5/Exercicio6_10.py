# Program: Exercicio6_10.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 15:51
# Updated:

number1 = int(input("Entre com o primeiro número para ser pesquisado na lista: "))
number2 = int(input("Entre com o segundo número para ser pesquisado na lista: "))
cont = 0
numb1 = -1
numb2 = -1
#bigger = len(lista)
contador1 = "NOK"
contador2 = "NOK"
lista = list(range(1, 18))
while cont<len(lista):
    if (number1 == lista[cont]):
        print("Número %d encontrado, na posição %d."%(lista[cont], cont))
        contador1 = "Ok"
        numb1 = cont
    if (number2 == lista[cont]):
        print("Número %d encontrado, na posição %d."%(lista[cont], cont))
        contador2 = "Ok"
        numb1 = cont
    if((cont==(len(lista)-1)) and (contador1 == "NOK")):
        print("Número não encontrado: %d" %number1)
    if((cont==(len(lista)-1)) and (contador2 == "NOK")):
        print("Número não encontrado: %d" %number2)
    cont+=1
if(numb1!=-1)and(numb1!=-1):
    if numb2>=numb1:
        print("%d foi encontrado primeiro." %number1)
    else:
        print("%d foi encontrado primeiro." %number2)
else:
    print("Alguns dos números ou od ois não foram encontrados.")
