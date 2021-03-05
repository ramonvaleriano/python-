# Program: desafio_072.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 21:31

tupla_preenchida = tuple(range(0, 21))
print(tupla_preenchida)
number = int(input('Digite um número: '))
while number is not tupla_preenchida:
    number = int(input('Tente novamente. Digite um número: '))
    if number in tupla_preenchida:
        indice = tupla_preenchida.index(number)
        break
print(f'A posiçãao é: {indice}')