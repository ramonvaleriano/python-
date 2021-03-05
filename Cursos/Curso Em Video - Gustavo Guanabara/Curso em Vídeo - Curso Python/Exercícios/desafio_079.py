# Program: desafio_079.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 02/10/2020 - 19:49

numeros = list()
number = float(input('Digite um número: '))
numeros.append(number)

while True:
    resposta = str(input('Você deseja adicionar mais um número[S/N]: ')).upper()[0]
    if resposta == 'N':
        print(f'Fim do Programa!')
        break
    elif resposta == 'S':
        number = float(input('Digite um número: '))
        if number in numeros:
            continue
        else:
            numeros.append(number)
    else:
        print('Respoda invalida!')

em_ordem = numeros.sort()
print(em_ordem)
