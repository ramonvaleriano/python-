# Program: Algoritmo320_Enq59.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/04/2020 - 10:04
# Updated:

cont = 0
note = float("Enter with the %d note: " %(cont+1))
sum_ = 0

while note>=0:
    cont+=1
    sum_+=note
    parcial = ((note**2)/cont)
    note = float("Enter with the %d note: " %(cont+1))
media = sum_/cont
variacao = parcial - (media**2)
print()
print(media)
print(variacao)
