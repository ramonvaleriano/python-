# Program: listagem8_15.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 17/09/2020 - 06:31

def valida(number, superiror, inferior):
    if number <= superiror and number >= inferior:
        print("Número dentro do permitido.")
    else:
        print("Número fora do permitido!")

numero = int(input("Digite um número: "))
max_ = int(input("Digite o número máximo permitido: "))
min_ = int(input("Digite o número mínimo permitido: "))

valida(numero, max_, min_)