# Program: listagem10_13.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 23:09

class ListaUnica:
    def __init__(self, elem_class):
        self._lista = list()
        self._elem_class = elem_class

    def __len__(self):
        return len(self._lista)

    def __iter__(self):
        return iter(self._lista)

    def __getitem__(self, item):
        return self._lista[item]

    def indiceValido(self, i):
        return i>=0 and i<len(self._lista)

    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self._lista.append(elem)

    def remove(self, elem):
        if len(self._lista) > 0:
            self._lista.remove(elem)

    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self._lista.index(elem)
        except ValueError:
            return -1

    def verifica_tipo(self, elem):
        if type(elem)!=self._elem_class:
            raise TypeError("Tipo Invalido")

    def ordenada(self, chave = None):
        self._lista.sort(key=chave)

lu = ListaUnica(int)