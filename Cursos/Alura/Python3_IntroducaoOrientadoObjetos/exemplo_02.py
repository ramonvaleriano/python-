# Program: exemplo1.py
# Author: Ramon R. Valeriano
# Description: Programa simples para similiar uma conta de banco e introduzir o conseito de Orientação a Objetos
# Developed: 18/02/2020 - 15:23

numero = 123
titular = 'Nico'
saldo = 55.0
limite = 1000.0

print(f'O número da conta {numero}, o títular {titular}, O saldo R$ {saldo} e o limite R${limite}')

conta = {
    "numero":123,
    'titular':'Nico',
    'saldo':55.0,
    'limite':1000.0
}

print(f'O número da conta {conta["numero"]}, o títular {conta["titular"]}, O saldo R$ {conta["saldo"]} '
      f'e o limite R${conta["limite"]}')
