# Program: desafio_065.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 15:58

cont = 0
soma = 0
maior = 0
menor = 0

while True:
    desejo = str(input('Deseja Adicionar um novo número: [S/N]')).upper().strip()
    if desejo == 'N':
        break
    elif desejo == 'S':
        number = int(input('Digite um número: '))
        soma+=number
        if cont == 0:
            maior = number
            menor = number
        cont+=1
        if number >= maior:
            maior = number
        elif number <= menor:
            menor = number
    else:
        print('Opção Invalida!')

media = soma/cont
print(media)
print(cont)
print(maior)
print(menor)
