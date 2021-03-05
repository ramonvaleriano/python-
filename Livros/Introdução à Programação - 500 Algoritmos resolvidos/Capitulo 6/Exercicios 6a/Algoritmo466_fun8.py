# Program: Algoritmo466_fun8.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 08/06/2020 - 09:18
# Updated:

def trimestre(number):
    if number == 1:
        return("Janeiro")
    elif number == 2:
        return("Fevereiro")
    elif number == 3:
        return("Março")
    else:
        return("Opção Invalida")

def exibir(number, funcao):
    message = funcao(number)
    print(message)

s = "Digite um número desejado"
q = len(s)+5
print("*"*(q+2))
number = int(input(("X"+s.center(q, "*")+"X\n")))
print("+"*(q+2))
exibir(number, trimestre)


