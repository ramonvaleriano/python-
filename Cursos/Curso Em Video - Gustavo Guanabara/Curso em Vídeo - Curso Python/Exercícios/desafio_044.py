# Program: desafio_044.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 19:27

valor = float(input('Digite o valor do produto: '))
if valor > 0:
    opcao = int(input('Digite a forma de pagamento: '))
    if opcao == 1:
        new_valor = valor - ((valor*10)/100)
        print(new_valor)
    elif opcao == 2:
        new_valor = valor - ((valor*5)/100)
        print(new_valor)
    elif opcao == 3:
        new_valor = valor
        print(new_valor)
    elif opcao == 4:
        new_valor = valor + ((valor * 20) / 100)
        print(new_valor)
    else:
        print('Opção invalida!')
else:
    print('Valor Invalido!')