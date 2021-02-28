# Program: banco.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 21:37

class Banco:
    def __init__(self, nome):
        self._nome = nome
        self.clientes = list()
        self.contas = list()

    def abre_conta(self, conta):
        return self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()


