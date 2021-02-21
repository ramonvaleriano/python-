# Program: listagem10_1_1.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 21/02/2020 - 16:19

class Televisao:
    def __init__(self):
        self.__ligada = False
        self.__canal = 2

    @property
    def ligada(self):
        return self.__ligada

    @ligada.setter
    def ligada(self, valor):
        self.__ligada = valor
        return self.__ligada

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, valor):
        self.__canal = valor
        return self.__canal


tv = Televisao()
print(tv.ligada)
print(tv.canal)
tv.canal = 6
print(tv.canal)