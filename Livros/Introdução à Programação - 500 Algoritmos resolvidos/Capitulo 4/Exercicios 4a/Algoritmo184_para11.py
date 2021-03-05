# Program: Algoritmo184_para11.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 10:25
# Updated:

import math

for e in range(8):
    number = float(input("Enter with %d° number: " %(e+1)))
    result = (math.log(number)/math.log(10))
    print(result, "\n")
