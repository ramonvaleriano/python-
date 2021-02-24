# Program: exercicio10_7.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 24/02/2020 - 10:28

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.__clientes = clientes
        self.__numero = numero
        self.__saldo = 0
        self.__operacoes = list()
        self.deposito(saldo)

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

    @property
    def saldo(self):
        return self.__saldo

    def resumo(self):
        print(f'CC número {self.__numero}, Saldo: R$ {self.__saldo}')

    def saque(self, valor):
        if self.__saldo >= valor:
            self.__saldo-= valor
            self.__operacoes.append(["Saque", valor])
        else:
            print(f'Saldo Insuficente!')

    def deposito(self, valor):
        if valor>=0:
            self.__saldo+=valor
            self.__operacoes.append(["Deposito", valor])

    @property
    def extrado(self):
        for c in self.__clientes:
            print(f'{c[0]} = {c[1]}')
        if len(self.__operacoes)>0:
            for o in self.__operacoes:
                print(f'{o[0]} - {o[1]}')
            print(f'\n Saldo: {self.__saldo}')
        else:
            print("Não houve qualquer tipo de operação.")

