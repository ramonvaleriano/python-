# Program: contas.py
# Author: Ramon R. Valeriano
# Decription: Modulo que será usado para os próximos exmplos
# Developed: 24/02/2020 - 09:26

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.__clientes = clientes
        self.__numero = numero
        self.__saldo = saldo

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clintes(self, novos_clientes):
        self.__clientes = novos_clientes
        return self.__clientes

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
        return self.__numero

    def resumo(self):
        print(f'CC número {self.__numero}, Saldo: R$ {self.__saldo}')

    def saque(self, valor):
        if self.__saldo >= valor:
            self.__saldo-= valor

    def deposito(self, valor):
        if valor>=0:
            self.__saldo+=valor



