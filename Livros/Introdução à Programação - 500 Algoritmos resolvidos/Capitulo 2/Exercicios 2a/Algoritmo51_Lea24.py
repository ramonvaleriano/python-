# Program: Algoritmo51_Lea24.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/03/2020 - 17:54
# Updated:

import math

radius = float(input("Enter with the radius of a circle: "))
numberPi= math.pi
perimeter = 2*numberPi*radius
area = numberPi*(radius**2)

print("%5.2f\n%5.2f\n" %(perimeter,area))
