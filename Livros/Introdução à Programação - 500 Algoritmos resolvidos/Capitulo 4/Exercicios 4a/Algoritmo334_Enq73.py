# Program: Algoritmo334_Enq73.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/04/2020 - 19:02
# Updated:

smaller = 0
bigger = 0
cont = 0
code_b = 0
code_s = 0

while True:
    code = int(input("Enter with the code: "))
    if code <=0:
        break
    weight = float(input("Enter with the weight: "))
    if cont == 0  and weight > 0:
        bigger = weight
        smaller = weight
        code_b = code
        code_s = code
    if weight > 0:
        cont+=1
        if weight >= bigger:
            bigger = weight
            code_b = code
        elif weight <= bigger:
            smaller = weight
            code_s = code
    else:
        print("Invalid Option!")
print()
print(bigger)
print(smaller)
print(code_b)
print(code_s)
