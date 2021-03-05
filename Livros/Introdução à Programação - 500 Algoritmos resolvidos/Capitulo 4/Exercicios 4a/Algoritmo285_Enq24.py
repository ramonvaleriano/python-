# Program: Algoritmo285_Enq24.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/04/2020 - 17:35
# Updated:

dividendo = int(input("Entre com o número que será dividido: "))
divisor = int(input("Entre com o número que será o divisor: "))
resto = 0
quociente = 0
while dividendo>=divisor:
    dividendo-=divisor
    quociente+=1
resto = dividendo
print(quociente)
print(resto)
