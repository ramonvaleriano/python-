# Program: Algoritmo160_se71.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 14:52
# Updated:

number = float(input("Enter with a number: "))

if number<=1:
    result = 1
elif(number>1)and(number<=2):
    result = 2
elif(number>2)and(number<=3):
    result = (number**2)
elif number>3:
    result = (number**3)
else:
    result = 0
print(result)

