# Program: Algoritmo147_se58.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 09:50
# Updated:

plate = input("Enter with the plate: ")

plate = plate.upper()
sum_ = 0
value = 0
if(plate == "VEGETARIANO"):
    value = 180
    sum_+=value
elif(plate == "PEIXE"):
    value = 130
    sum_+=value
elif(plate == "FRANGO"):
    value = 250
    sum_+=value
elif(plate == "CARNE"):
    value = 350
    sum_+=value
else:
    value = 0
    sum_+=value
#sum_+=value

sobremesa = input("Enter with the dessert: ")

sobremesa = plate.upper()

sum_1 = 0
value1 = 0

if(sobremesa == "ABACAXI"):
    value1 = 75
    sum_1+=value1
elif(sobremesa == "SORVETE"):
    value = 110
    sum_1+=value1
elif(sobremesa == "MOUSSE"):
    value = 170
    sum_1+=value1
elif(sobremesa == "CHOCOLATE"):
    value = 200
    sum_1+=value1
else:
    value = 0
total = sum_ + sum_1
print(total)
print(plate)
print(sobremesa)

