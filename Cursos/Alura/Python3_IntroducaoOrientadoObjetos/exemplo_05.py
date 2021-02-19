# Program: exemplo_05.py
# Author: Ramon R. Valeriano
# Description: Primeiro programa que usa de fato o paradigma Orientado a Objeto.
# Developed: 19/02/2020 - 09:56

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123, "Ramon", 55.0, 1000)
conta1 = Conta(321, "Milla", 50000, 3000)
print(conta.titular)
print(conta.saldo)
print(conta1.titular)
print(conta1.saldo)