# Program: orcamento_ex_cap02.py
# Author: Ramon R. Valeriano
# Description: Todos os orçamentos que nós necessitamos estarão aqui
# Developed: 21/04/2021 - 06:37

class Orcamento:

    def __init__(self):
        self.__itens = list()

    @property
    def valor(self):
        total = 0
        for item in self.__itens:
            total+=item

        return total

    def iten(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item.valor)

class Item:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor