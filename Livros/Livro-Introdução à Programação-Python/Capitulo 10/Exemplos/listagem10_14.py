# Program: listagem10_14.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 23:29

class Nome:
    def __init__(self, nome):
        if nome == None or not nome.strip():
            raise ValueError('Nome não pode ser Nulo nem em Branco')
        self._nome = nome
        self.chave = nome.strip().lower()

    def __str__(self):
        return self._nome

    def __repr__(self):
        return f'<Class {type(self).__name__} em 0x{id(self)} Nome: {self._nome} Chave: {self.chave}'

    def __eq__(self, other):
        print('__eq__ Chamado!')
        return self._nome == other.nome

    def __lt__(self, other):
        print('__lt__ Chamado!')
        return self._nome < other.nome