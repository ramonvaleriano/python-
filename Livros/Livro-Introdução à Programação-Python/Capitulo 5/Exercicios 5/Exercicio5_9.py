# Program: Exercicio5_9.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 29/03/2020 - 12:13
# Update:

dividendo = int(input("Entre com o dividendo: "))
divisor = int(input("Entre com o divisor: "))
quociente = 0
aux = dividendo

while aux >= divisor:
    aux-=divisor
    quociente+=1
resto = aux
print(quociente)
print(resto)
