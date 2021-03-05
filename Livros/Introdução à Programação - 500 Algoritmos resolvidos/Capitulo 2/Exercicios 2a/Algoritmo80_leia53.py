# Program: Algoritmo80_leia53.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/03/2020 - 19:04
# Updated:

tapes = int(input("Enter with the quantity of tapes: "))
rent = float(input("Enter with the value of rent: "))

third = ((tapes/3)*rent)*12
mulct = rent+(rent*10)/100
tapes_mulct = (tapes/10)*mulct
minimun = tapes - ((tapes*2)/100)

print(third)
print(tapes_mulct)
print(minimun)



