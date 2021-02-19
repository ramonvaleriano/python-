# Program: exemplo_08.py
# Author: Ramon R. Valeriano
# Description: Criando Metodos
# Developed: 19/02/2020 - 11:47

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O Saldo R$ {self.__saldo} do Titular {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)


conta1 = Conta(123, "Ramon", 55.0, 1000.0)
conta2 = Conta(321, "Milla", 50000, 3000.0)

conta2.transferir(34.0, conta2, conta1)
print(conta1.extrato())
print(conta2.extrato())