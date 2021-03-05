# Program: desafio_064.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 15:39

cont = 0
soma = 0
number = 0
while number != 999:
    number = int(input('Digite um número por favor: '))
    if number != 999:
        cont+=1
        soma+=number
print(cont)
print(soma)