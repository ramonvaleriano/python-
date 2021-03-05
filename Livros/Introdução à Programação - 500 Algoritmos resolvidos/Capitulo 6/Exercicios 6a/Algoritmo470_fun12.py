# Program: Algoritmo470_fun12.py
# Author: Ramon R. Valerino
# Description:
# Developed: 08/06/2020 - 11:05
# Updated:

def verificando(number):
    cont = 1
    test = 0
    while number>=cont:
        if number%cont==0:
            test+=1
        cont+=1
    return test

def condicional(number, funcao):
    if funcao(number) == 2 or number == 1:
        return("É um número primo!")
    else:
        return("Não é um número primo!")
            
numero = int(input("Digite um número qualquer: "))
print(condicional(numero, verificando))
