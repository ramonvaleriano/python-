# Program: listagem10_1_1.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 21/02/2020 - 16:41

class Televisao:
    def __init__(self):
        self.__ligada = False
        self.__canal = 2

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
        self.canal-=1

    def mudar_canal_para_cima(self):
        self.canal+=1


tv = Televisao()
print(tv.ligada)
tv.ligada = True
tv.canal = 9
print(tv.ligada)
print(tv.canal)
tv.mudar_canal_para_cima()
tv.mudar_canal_para_cima()
print(tv.canal)
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.mudar_canal_para_baixo()
print(tv_sala.canal)