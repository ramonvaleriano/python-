# Program: Algoritmo189_para16.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 10:51
# Updated:

higher = int(input("Enter with the higher limit: "))
bottom = int(input("Enter with the bottom limit: "))
increment = int(input("Enter with the increment number: "))

if((higher>bottom)and(type(increment) is int)):
    for e in range(bottom, higher+1, increment):
        result = (5*(e-32))/9
        print(result, "\n")
else:
    print("Invalid Option!")
