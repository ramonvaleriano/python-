# Program: Algoritmo153_se64.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 13:39
# Updated:

indice = float(input("Entre com o indice:"))

if indice > 0:
    if indice >= 0.5:
        print("Suspende os grupos 1, 2 e 3!")
    elif(indice<0.5)and(indice>=0.4):
        print("Supende os grupos 1 e 2!")
    elif(indice<0.4)and(indice>=0.3):
        print("Suspende o Grupo 1")
    else:
        print("Faça porra alguma, caralho")
else:
    print("Vá se fuder!")
