# Program: Algoritmo89_PesoDoPlaneta.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/03/2020 - 08:34
# Updated:

weight = float(input("Enter with your weight: "))
planet=int(input("Witch Planet: "))

if planet == 1:
    gravity = 0.37
elif planet == 2:
    gravity = 0.88
elif planet == 3:
    gravity = 0.38
elif planet == 4:
    gravity = 2.64
elif planet == 5:
    gravity = 1.15
elif planet == 6:
    gravity = 1.17
else:
    gravity = 0
result = weight*(gravity/10)*9.89
print(result)
