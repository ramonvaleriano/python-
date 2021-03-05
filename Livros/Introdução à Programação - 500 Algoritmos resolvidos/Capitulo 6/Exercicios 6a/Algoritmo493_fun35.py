# Program: Algoritmo493_fun35.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 10:15 
# Updated:

def decrescente(lista):
    cont = (len(lista)-1)
    test = "ok"
    while True:
        if cont == 0:
            break
        if(lista[cont]>lista[cont-1]):
            testando = True
        else:
            test = "nok"
            testando = False
        cont-=1
    if test == "ok":
        return True
    else:
        return False

def crescente(lista):
    cont = (len(lista)-1)
    c = 0
    test = "ok"
    while True:
        if cont == c:
            break
        if(lista[c]>lista[c+1]):
            testando = True
        else:
            test = "nok"
            testando = False
        c+=1
    if test == "ok":
        return True
    else:
        return False

def mensagem(teste1, teste2, lista):
    if(teste1(lista)):
        print("Está em ordem Crescente")
    elif(teste2(lista)):
        print("Está em ordem Decrescente")
    else:
        print("não há ordem alguma!")

lista = list()

for e in range(10):
    number = int(input("Entre com um  número: "))
    lista.append(number)

mensagem(crescente, decrescente, lista)
