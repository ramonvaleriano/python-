# Program: Listagem5_16.py 
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 10:31
# Updated:

tabuada = 1
numero = 1
while tabuada<=10:
    soma = numero+tabuada
    print("%02d + %02d = %02d" %(tabuada, numero, soma))
    numero+=1
    if numero == 11:
        numero = 1
        tabuada+=1
        print()
