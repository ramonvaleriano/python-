# Program: exercicio10_1_1.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 21/02/2020 - 16:30

class Televisao:
    def __init__(self):
        self.__ligada = False
        self.__canal = 2
        self.__tamanho = "29 Polegadas"
        self.__marca = "Lg"

    @property
    def ligada(self):
        return self.__ligada

    @ligada.setter
    def ligada(self, estado):
        self.__ligada = estado
        return self.__ligada

    @property
    def canal(self):
        return self.__ligada

    @canal.setter
    def canal(self, valor):
        self.__canal = valor
        return self.__canal

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, polegadas):
        self.__tamanho = polegadas
        return self.__tamanho

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, nome):
        self.__marca = nome
        return self.__marca

