# Program: Algoritmo296_Enq35.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 07:17
# Updated:

tax = 30
temp = 0.30
conversion = 1
while True:
    mass = float(input("Enter with the quantity of Massa: "))
    if mass<=0:
        break
    while mass>=0.10:
        mass-=((mass*tax)/100)
        print(mass)
        temp+=0.30
    print(temp)
    
