# Program: 2.py
# Author: Ramon R. Valeriano
# Decription: Modulo que será usado para os próximos exmplos
# Developed: 24/02/2020 - 09:53

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
        self.operacoes = list()
        self.deposito(saldo)

    @property
    def clientes(self):
        return self.clientes

    @clientes.setter
    def clintes(self, novos_clientes):
        self.clientes = novos_clientes
        return self.clientes

    @property
    def numero(self):
        return self.numero

    @numero.setter
    def numero(self, novo_numero):
        self.numero = novo_numero
        return self.numero

    @property
    def saldo(self):
        return self.saldo

    def resumo(self):
        print(f'CC número {self.numero}, Saldo: R$ {self.saldo}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo-= valor
            self.operacoes.append(["Saque", valor])

    def deposito(self, valor):
        if valor>=0:
            self.saldo+=valor
            self.operacoes.append(["Deposito", valor])

    @property
    def extrado(self):
        if len(self.operacoes)>0:
            for o in self.operacoes:
                print(f'{o[0]}-{o[1]}')
            print(f'\n Saldo: {self.saldo}')
        else:
            print("Não houve qualquer tipo de operação.")

