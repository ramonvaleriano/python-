# Program: numeros_primos.py
# Author: Ramon R. Valerino
# Description:
# Developed: 08/06/2020 - 11:05
# Updated: 08/06/2020 - 13:06

def analise(number):
    cont = 1
    test = 0
    while number>=cont:
        if number%cont==0:
            test+=1
        cont+=1
    return test

def verificando(number, testando):
    if(testando(number) == 2) or (number == 1):
        return True
    else:
        return False

def serie(number, validando, testando):
    lista_primos = list()
    for e in range(number+1):
        if validando(e, testando):
            lista_primos.append(e)
            print(e, end=" ")
    print()

def mensagem(number, validando, testando):
    if(validando(number, testando)):
        print("É um número primo!")
    else:
        print("Não é um número primo!")




    
