# Programa: Algoritmo132_se43.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 12:19
# Updated:

real_brazilian = float(input("Enter with the value: "))
currency = input("Enter with currency: ")

first = currency[0]

if real_brazilian >0:
    if(currency=="f")or(currency=="F"):
        value = float(input("Enter with the value of Franco: "))
        conversion = real_brazilian / value
    elif(currency=="l")or(currency=="L"):
        value = float(input("Enter with the value of Libra: "))
        conversion = real_brazilian / value
    elif(currency=="d")or(currency=="D"):
        value = float(input("Enter with the value of Dolar: "))
        conversion = real_brazilian / value
    elif(currency=="m")or(currency=="M"):
        value = float(input("Enter with the value of Marco: "))
        conversion = real_brazilian / value
    else:
        print("Not Exist!")
        value = 1
        conversion = real_brazilian / value
else:
    print("What fuck is This?!")

print(conversion)


    
