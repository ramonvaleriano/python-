# Programa: Algoritmo133_se44.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 12:34
# Updated:

height = float(input("Enter with your height: "))
weight = float(input("Enter with your weght: "))
sex = input("Enter with your sex in portuguese: ")

sex = sex.upper()

if sex=="MASCULINO":
    calculation = (72.7 * height)-58
    if weight > calculation:
        print("Você está ácima do peso! ")
        print(calculation)
    else:
        print("Ideal weight!")
        print(calculation)
elif sex=="FEMININO":
    calculation = (62.1 * height)-44.7
    if weight > calculation:
        print("Você está ácima do peso! ")
        print(calculation)
    else:
        print("Ideal weight!")
        print(calculation)
else:
    print("What fuck is this?!")

print(sex)
