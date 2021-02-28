# Program: nome3.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 28/02/2020 - 11:59

from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'<Class {type(self).__name__} em 0x{id(self):x} Nome: {self.nome}'

    def __eq__(self, outro):
        print('__eq__ Chamado')
        return self.nome == outro

    def __lt__(self, outro):
        print('__lt__ Chamado')
        return self.nome < outro

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor == None or not valor.strip():
            raise ValueError('Nome não pode ser nulo nem em branco.')
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @property
    def chave(self):
        return self.__chave

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()