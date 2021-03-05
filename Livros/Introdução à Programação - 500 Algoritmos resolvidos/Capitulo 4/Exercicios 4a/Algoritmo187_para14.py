# Program: Algoritmo187_para14.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 10:41
# Updated:

numerator = int(input("Enter with the numerator: "))
exponent = int(input("Enter with the Exponent: "))
result = 1
if((type(numerator) is int)and(type(exponent) is int)and(numerator>=1)and(exponent>=2)):
    for e in range(exponent):
        result*=numerator
    print(result)
else:
    print("Invalid Option!")
