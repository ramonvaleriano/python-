# Program: exemplo_03.py
# Author: Ramon R. Valeriano
# Description: Programa simples para similiar uma conta de banco e introduzir o conseito de Orientação a Objetos
# Developed: 19/02/2020 - 08:54

def criar_conta(numero, titular, saldo, limite):
    conta = {
        "numero":numero,
        'titular':titular,
        'saldo':saldo,
        'limite':limite
    }
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f'O saldo é: R$ {conta["saldo"]}')

conta = criar_conta(123654, 'Ramon', 0, 1000)
depositar(conta, 100)
sacar(conta, 35)
extrato(conta)