# Program: Algoritmo52_Lea25.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/03/2020 - 18:01
# Updated:

import math

side = float(input("Enter with a side of a square: "))

area = side**2
diagonal = side*math.sqrt(2)
perimeter = 4*side


print("%05.2f\n%05.2f\n%05.2f\n" %(area, diagonal, perimeter))
