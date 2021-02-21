# Program: Exercicio8_3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 11:32
# Updated:

def area_quadrado(lado):
    if lado>=0:
        area = lado**2
        return area
    else:
        return 0
lado = float(input("Entre com o lado da área que deseja calcular: "))
area = area_quadrado(lado)
print(area)
