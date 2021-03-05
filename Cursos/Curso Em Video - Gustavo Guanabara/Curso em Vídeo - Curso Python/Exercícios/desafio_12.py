# Programa: desafio_12.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 22:59

def entrada():
    valor = float(input("Digite o valor do produto: "))
    return valor

def desconto(funcao):
    test = funcao()
    new_valor = test - ((test*5)/100)
    return new_valor

final = desconto(entrada)
print(final)
