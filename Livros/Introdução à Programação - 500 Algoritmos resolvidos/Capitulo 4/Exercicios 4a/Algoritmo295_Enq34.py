# Program: Algoritmo295_Enq34.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 07:09
# Updated:

bigger = 0
while True:
    name = input("Enter with the name of the product: ")
    name = name.upper()
    if name == "FIM":
        break
    quantity = int(input("Enter with the quantity of the product: "))
    sold = int(input("Enter with the sold quantity: "))
    result = quantity - sold
    if result <= 50:
        print(name)
        print(result)
    if bigger<=result:
        bigger = result
        name_b = name
print(result)
print(name)
