# Program: clientes.py
# Author: Ramon R. Valeriano
# Decription: Modulo que será usado para os próximos exmplos
# Developed: 24/02/2020 - 09:16

class Cliente:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
        return self.__telefone