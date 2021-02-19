# Program: exemplo_12.py
# Author: Ramon R. Valeriano
# Description: Criando Metodos
# Developed: 19/02/2020 - 15:53

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
        if(valor <= (self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            print(f'O Valor R${valor} ultrapassa o limite.')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite






conta1 = Conta(123, "Ramon", 55.0, 1000.0)
conta2 = Conta(321, "Milla", 50000, 3000.0)

conta2.transferir(34.0, conta1)
print(conta1.extrato())
print(conta2.extrato())

print(conta1.limite)
conta1.limite = 2000.0
print(conta1.limite)

conta1.sacar(2345)
print(conta1.saldo)