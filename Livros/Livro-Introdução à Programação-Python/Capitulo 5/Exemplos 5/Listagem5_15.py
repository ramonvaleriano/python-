# Program: Listagem5_15.py 
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 10:17
# Updated:

tabuada = 1

while tabuada<=10:
    numero = 1
    while numero<=10:
        soma = numero+tabuada
        print("%02d + %02d = %02d" %(tabuada, numero, soma))
        numero+=1
    print()
    tabuada+=1

