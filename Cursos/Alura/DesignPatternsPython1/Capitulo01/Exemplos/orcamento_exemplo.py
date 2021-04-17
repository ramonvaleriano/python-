# Program: orcamento_exemplo.py
# Author: Ramon R. Valeriano
# Description: Todos os orçamentos que nós necessitamos estarão aqui
# Developed: 16/04/2021 - 20:48

class Orcamento:

    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

