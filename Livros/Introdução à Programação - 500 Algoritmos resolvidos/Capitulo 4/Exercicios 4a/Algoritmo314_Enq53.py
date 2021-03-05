# Program: Algoritmo314_Enq53.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 10:46
# Updated:

sum_l = 0
sum_a = 0
sum_h = 0
sum_day = 0

while True:
    value = float(input("Enter with the value of the product: "))
    if value == 0:
        break
    print("'L' - Limpeza")
    print("'A' - Alimentação")
    print("'H' - Higiene")
    code = input("Enter with code of the product: ")
    code = code.upper()
    sum_day+=value
    if code == "L":
        sum_l+=value
    elif code == "A":
        sum_a+=value
    elif code == "H":
        sum_h+=value
    else:
        print("Invalid Option!")
    print()
print(sum_day)
print(sum_l)
print(sum_a)
print(sum_h)
