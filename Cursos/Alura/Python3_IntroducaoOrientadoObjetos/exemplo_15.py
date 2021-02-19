# Program: exemplo_15.py
# Author: Ramon R. Valeriano
# Description: Metodos privados
# Developed: 19/02/2020 - 16:13

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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"bb":"001", "Caixa":"002", "Bradesco":"237"}




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

print(Conta.codigo_banco())
print(Conta.codigos_bancos())