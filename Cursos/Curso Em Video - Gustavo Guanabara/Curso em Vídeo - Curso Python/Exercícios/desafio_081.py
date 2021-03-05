# Program: desafio_081.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 05/10/2020 - 07:43

numeros = list()
cont = 0
verification = False

while True:
    number = int(input('Digite um número: '))
    numeros.append(number)
    cont+=1
    if number == 5:
        verification = True
    opcao = str(input('Você ainda deseja escrever mais um número [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        print('Finalizando o Programa: ')
        break
c = 0
quantidade = len(numeros)
while c<quantidade:
    s = 0
    while s<(quantidade-1):
        if numeros[c]>=numeros[s]:
            numeros[c], numeros[s] = numeros[s], numeros[c]
        s+=1
    c+=1

print(f'Foram digitado {cont} números ao total.')

if verification:
    lugar = numeros.count(5)
    print(f'O número 5 foi encontrado na posição: {lugar}')