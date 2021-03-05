# Program: Algoritmo50_Lea23.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/03/2020 - 17:40
# Updated:

import math

base = float(input("Enter with the base of a triangule: "))
height = float(input("Enter with the height of a triangule: "))

perimeter = base*height
area = (height*base)/2 
diagonal = math.sqrt((base**2)+(height**2))

print("%05.2f\n%05.2f\n%05.2f" %(perimeter,area,diagonal))
