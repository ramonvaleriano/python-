# Program: listagem10_9.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 21:41

class Banco:
    def __init__(self, nome):
        self._nome = nome
        self.clientes = list()
        self.contas = list()

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        return self._nome

    def abre_conta(self, conta):
        return self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()





