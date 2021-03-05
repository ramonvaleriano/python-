# Program: aula_15c.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 16:50

cont = soma = 0

while True:
    number = int(input('Digite um número: '))
    if number == 999:
        break
    cont+=1
    soma+=number
print(soma)
print(cont)