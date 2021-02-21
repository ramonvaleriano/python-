# Program: listagem10_1.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 08/02/2020 - 07:47

class Televisao:
    def __init__(self):
        self.ligada=False
        self.canal=2


tv = Televisao()
print(tv.ligada)
print(tv.canal)

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
print(tv_sala.ligada)
print(tv_sala.canal)

tv_quarto = Televisao()
print(tv_quarto.ligada)
print(tv_quarto.canal)
