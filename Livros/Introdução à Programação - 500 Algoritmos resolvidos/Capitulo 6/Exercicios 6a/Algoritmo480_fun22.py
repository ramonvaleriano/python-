# Program: Algoritmo480_fun22.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/06/2020 - 18:00
# Updated:

def reversao(number):
    test = str(number)
    test = list(test)
    quantity = len(test)
    retro = list()
    for e in range((quantity-1), -1, -1):
        retro.append(test[e])
    #print(retro)
    return retro
    
    
def comparacao(inverso, number):
    invertido = inverso(number)
    lista = str(number)
    lista = list(lista)
    #print(lista)
    quantity = len(lista)
    answer =(invertido==lista)
    #print(answer)
    return answer
    

def mensagem(resposta, inverso, number):
    if resposta(inverso, number):
        print("É um número Capicua")
    else:
        print("Não é porra alguma!")

number = int(input("Enter with the number: "))
mensagem(comparacao, reversao, number)

    
