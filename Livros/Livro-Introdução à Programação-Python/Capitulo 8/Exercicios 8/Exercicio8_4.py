# Program: Exercicio8_4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 11:38
# Updated:

def area_triangulo(base, altura):
    if base>=0 and altura>=0:
        area = ((base*altura)/2)
        return area
    else:
        return 0
base = float(input("Enter com a base de um triângulo: "))
altura = float(input("Entre com a altura do triângulo: "))

area = area_triangulo(base, altura)
print(area)
