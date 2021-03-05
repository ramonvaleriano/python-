# Program: desafio_055.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 28/09/2020 - 21:22

maior = 0
menor = 0
quantidade = 5

for i in range(quantidade):
    peso = float(input('Digite o peso da %d pessoa: ' %(i+1)))
    if i == 0:
        maior = peso
        menor = peso
    elif peso>=maior:
        maior = peso
    elif peso<=menor:
        menor = peso
print(maior)
print(menor)