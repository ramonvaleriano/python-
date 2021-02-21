# Program: listagem10_3.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 21/02/2020 - 16:57

class Televisao:
    def __init__(self, min, max):
        self.__ligada = False
        self.__canal = 2
        self.__min = min
        self.__max = max

    @property
    def ligada(self):
        return self.__ligada

    @ligada.setter
    def ligada(self, estado):
        self.__ligada = estado
        return self.__ligada

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, valor):
        self.__canal = valor
        return self.__canal

    def mudar_canal_para_baixo(self):
        if ((self.__canal-1)>=self.__min):
            self.__canal-=1

    def mudar_canal_para_cima(self):
        if ((self.__canal+1)<=self.__max):
            self.__canal+=1

tv_sala = Televisao(0, 10)
tv_sala.ligada = True
print("Estado da Tv da sala:", tv_sala.ligada)
print("Canal da Tv da Sala:", tv_sala.canal)
tv_sala.mudar_canal_para_baixo()
print("Canal da Tv da Sala:", tv_sala.canal)
tv_sala.mudar_canal_para_baixo()
print("Canal da Tv da Sala:", tv_sala.canal)
tv_sala.mudar_canal_para_baixo()
print("Canal da Tv da Sala:", tv_sala.canal)
tv_sala.mudar_canal_para_cima()
tv_sala.mudar_canal_para_cima()
tv_sala.mudar_canal_para_cima()
tv_sala.mudar_canal_para_cima()
tv_sala.mudar_canal_para_cima()
tv_sala.mudar_canal_para_cima()
tv_sala.mudar_canal_para_cima()
print("Canal da Tv da Sala:", tv_sala.canal)

