# Program: Algoritmo152_se62.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 12:07
# Updated:

weight = float(input("Enter with the your weight: "))
height = float(input("Enter with the your height: "))

if(weight>0)and(height>0):
    result = (weight)/(height**2)

    if result < 20:
        print("Abaixo do peso!")
    elif(result>=20)and(result<25):
        print("Normal")
    elif(result>=25)and(result<30):
        print("Excesso de peso!")
    elif(result>=30)and(result<35):
        print("Obesidade")
    elif(result>=35):
        print("Você vai morrer!")
    else:
        print("What fuck is this?!")
else:
    print("You are asshole!")
