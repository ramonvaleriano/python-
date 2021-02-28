# Program: clientes.py
# Author: Ramon R. Valeriano
# Decription: Modulo que será usado para os próximos exmplos
# Developed: 24/02/2020 - 09:16

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    @property
    def telefone(self):
        return self.telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.telefone = novo_telefone
        return self.telefone