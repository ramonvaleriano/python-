# Program: desafio_059.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 08:39

mensagem1 = 'Digite o 1° número: '
mensagem2 = 'Digite o 2° número: '
q_mens = len(mensagem2)

while True:
    print('='*q_mens)
    number1 = int(input(mensagem1))
    number2 = int(input(mensagem2))
    print(""" 
    Digite a opçaõ que você deseja:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa>>>
    """)
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = number1 + number2
        print(soma)
    elif opcao == 2:
        multiplica = number1 * number2
        print(multiplica)
    elif opcao == 4:
        print('Entrar com novos valores>>>>')
        continue
    elif opcao == 5:
        print('Sair do programa!')
    else:
        print('Opção Invalida!')
print('\mFim do Programa.')
