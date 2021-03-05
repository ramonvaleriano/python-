# Program: Algoritmo186_para13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 10:31
# Updated:

for e in range(4):
    number = float(input("Enter with %d° number: " %(e+1)))
    root_cubic = number**(1/3)
    cube = number**3
    print("%d - %d\n" %(root_cubic, cube))
