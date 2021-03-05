# Program: Algoritmo151_se61.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 11:56
# Updated:

import math

angle = float(input("Enter with the angle: "))

radians = math.radians(angle)
pi = math.pi

if(((radians>(pi/2))and(radians<=pi))or((radians>((3*pi)/2))and(radians<=(2*pi))):
   seno = math.sen(radians)
   print(seno)
else:
    cos = math.cos(radians)
    print(cos)
