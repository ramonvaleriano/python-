# Program: Algoritmo42_lea15.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/03/2020 - 20:19
# Updated:

import math

angle = float(input("Enter with the angle: "))

conversion = (math.pi*angle)/180
#print(conversion)
sin = math.sin(conversion)
cos = math.cos(conversion)
tan = math.tan(conversion)
atan = math.atan(conversion)
asin = math.asin(conversion)

print(conversion)
print(sin)
print(cos)
print(tan)
print(atan)
print(asin)
