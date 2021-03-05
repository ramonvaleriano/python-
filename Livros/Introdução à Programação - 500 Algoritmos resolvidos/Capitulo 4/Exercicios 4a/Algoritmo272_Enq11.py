# Program: Algoritmo272_Enq11.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 22:08
# Updated:

chico = 1.50
juca = 1.10
tax_chico = 0.02
tax_juca = 0.03
cont = 0

while juca<=chico:
    chico = chico + tax_chico
    juca = juca + tax_juca
    cont+=1
    print(cont)
