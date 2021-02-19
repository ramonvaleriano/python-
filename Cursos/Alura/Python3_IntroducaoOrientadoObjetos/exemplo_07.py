# Program: exemplo_07.py
# Author: Ramon R. Valeriano
# Description: Desafio Opcional
# Developed: 19/02/2020 - 11:36

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formaatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')


d = Data(19,2,2021)
d.formaatada()