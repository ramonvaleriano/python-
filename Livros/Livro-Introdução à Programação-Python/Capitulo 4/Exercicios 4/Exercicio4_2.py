# Program: Exercicio4_2.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 11:27
# Updated:

velocity =  float(input("Enter with your velocity: "))

if velocity > 80:
    print("Você foi multado!")
    unitary = velocity - 80
    value = unitary * 5
    print(value)
if velocity <= 80:
    print("Continue assim!")
