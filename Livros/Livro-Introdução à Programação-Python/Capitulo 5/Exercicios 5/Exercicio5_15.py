# Program: Exercicio5_15.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 09:07
# Updated:

sum_ = 0

while True:
    code = int(input("Enter with the code: "))
    if code == 0:
        break
    quantity = int(input("Enter with the quantity: "))
    if code == 1:
        value = 0.5*quantity
    elif code == 2:
        value = 1*quantity
    elif code == 3:
        value = 4*quantity
    elif code == 5:
        value = 7*quantity
    elif code == 9:
        value = 8*quantity
    else:
        print("Invalid code!")
    sum_+=value
print(sum_)
