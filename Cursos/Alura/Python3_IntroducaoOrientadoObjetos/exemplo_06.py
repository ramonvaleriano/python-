# Program: exemplo_06.py
# Author: Ramon R. Valeriano
# Description: Criando Metodos
# Developed: 19/02/2020 - 11:02

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O Saldo R$ {self.saldo} do Titular {self.titular}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

conta1 = Conta(123, "Ramon", 55.0, 1000)
conta2 = Conta(321, "Milla", 50000.00, 3000)

conta1.extrato()
conta2.extrato()

conta1.depositar(53.0)
conta2.sacar(2768)

conta1.extrato()
conta2.extrato()