# Program: exemplo_04.py
# Author: Ramon R. Valeriano
# Description: Primeiro programa que usa de fato o paradigma Orientado a Objeto.
# Developed: 19/02/2020 - 09:21

class Conta:
    def __init__(self):
        print('Contruindo um objeto')
        self.numero = 123
        self.titular = 'Ramon'
        self.saldo = 55.0
        self.limite = 1000


conta = Conta()
print(conta.numero)
print(conta.titular)
print(conta.saldo)
print(conta.limite)


