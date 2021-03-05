# Program: desafio_099.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 14:34

def maior(*numero):
    linha()
    print(f'Foram informados {len(numero)} valores')
    print(numero)
    maior = numero[0]
    for n in numero:
        if n>maior:
            maior = n
    print(f'O maior número é: {maior}')
    linha()


def linha():
    print('-='*20)


maior(1, 5, 2, 8, 30)
maior(4, 1, 7, 2, 6, 3, 0)
maior(1, 4, 2, 7)