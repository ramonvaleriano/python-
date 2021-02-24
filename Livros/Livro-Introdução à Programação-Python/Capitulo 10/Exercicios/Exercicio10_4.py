# Program: exercicio10_4.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 24/02/2020 - 08:50

class Televisao:
    def __init__(self, min=2, max=14):
        self.__min = min
        self.__max = max
        self.__ligada = False
        self.__canal = 2

    @property
    def ligada(self):
        return self.__ligada

    @ligada.setter
    def ligada(self, estado):
        self.__ligada = True
        return self.__ligada

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, valor):
        self.__canal = valor
        return self.__canal

    def mudar_canal_para_cima(self):
        if (self.__canal+1)<=(self.__max):
            self.__canal+=1
        if self.__canal == self.__max:
            self.__canal = self.__min

    def mudar_canal_para_baixo(self):
        if (self.__canal-1)>=(self.__min):
            self.__canal-=1
        if self.__canal == self.__min:
            self.canal = self.__max


tv = Televisao()
print(tv.canal)
tv_sala = Televisao(0, 10)
tv_sala.mudar_canal_para_baixo()
tv_sala.mudar_canal_para_baixo()
print(tv_sala.canal)