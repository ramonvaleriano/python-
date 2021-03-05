# Program: desafio_068.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 18:01

from random import randint

resultado = True

while True:
    print('=-'*20)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-' * 20)
    computador = randint(0, 10)
    number = int(input('Digite um número: '))
    opcao = str(input('Par ou Ímpar: [P/I]')).upper().strip()[0]
    soma = computador + number
    if opcao == 'P':
        if soma%2==0:
            #resultado = True
            print('Você venceu!')
            print(f'O computador jogou {computador} e você {number}')
        else:
            #resultado = False
            print('Você Perdeu!')
            print(f'O computador jogou {computador} e você {number}')
            break
    elif opcao == 'I':
        if soma%2!=0:
            #resultado = True
            print('Você venceu!')
            print(f'O computador jogou {computador} e você {number}')
        else:
            #resultado = False
            print('Você Perdeu!')
            print(f'O computador jogou {computador} e você {number}')
            break
    else:
        print('Opção Invalida!')
print('\nFim do Jogo!')