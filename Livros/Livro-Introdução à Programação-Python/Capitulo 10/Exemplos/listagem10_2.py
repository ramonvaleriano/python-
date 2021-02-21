# Program: listagem10_2.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 08/02/2020 - 08:02

class Televisao:
    def __init__(self):
        self.canal = 2
        self.ligada = False

    def mudar_canal_para_baixo(self):
        self.canal-=1

    def mudar_canal_para_cima(self):
        self.canal+=1

tv = Televisao()
print(tv.canal)
tv.mudar_canal_para_baixo()
print(tv.canal)
tv.mudar_canal_para_cima()
tv.mudar_canal_para_cima()
print(tv.canal)