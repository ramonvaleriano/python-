# Program: Algoritmo477_fun19.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/06/2020 - 15:24
# Updated:

def raiz_quadrada_exata(number):
    result =(number**(1/2))
    return(result%1==0)

def resposta(number, teste):
    if teste(number):
        print(1)
    else:
        print(0)

numero = int(input("Entrar com um número por favor: "))
resposta(numero, raiz_quadrada_exata)

