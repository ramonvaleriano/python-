# Program: Algoritmo271_Enq10.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 21:50
# Updated:

value_a = 5000000
value_b = 7000000
tax_a = 3
tax_b = 2
cont_a = value_a
cont_b = value_b
cont_total = 0
while value_a<=value_b:
    value_a = value_a + (value_a*tax_a)/100
    value_b = value_b + (value_b*tax_b)/100
    cont_total+=1
print(cont_total)
