# Program: exemplo_01.py
# Author: Ramon R. Valeriano
# Description: Programa simples para similiar uma conta de banco e introduzir o conseito de Orientação a Objetos
# Developed: 18/02/2020 - 15:28



def criar_conta(numero, titular, saldo, limite):
    conta = {
        "numero":numero,
        'titular':titular,
        'saldo':saldo,
        'limite':limite
    }
    return conta

conta = criar_conta(321, "Ramon", 0, 1000)

print(f'O número da conta {conta["numero"]}, o títular {conta["titular"]}, O saldo R$ {conta["saldo"]} '
      f'e o limite R${conta["limite"]}')
