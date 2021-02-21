# Program: exercicio10_1.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 08/02/2020 - 07:57

class Televisao:
    def __init__(self):
        self.ligada = False
        self.tamanho = 10
        self.canal = 2
        self.marca = 'isso ai'

tv = Televisao()
print(tv.ligada)
print(tv.tamanho)
print(tv.canal)
print(tv.marca)

tv_sala = Televisao
tv_sala.ligada = True
tv_sala.tamanho = 49
tv_sala.canal = 4
tv_sala.marca = 'LG'

print(tv_sala.ligada)
print(tv_sala.tamanho)
print(tv_sala.canal)
print(tv_sala.marca)

