# Program: Exercicio5_24.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 30/03/2020 - 11:38
# Updated:

number = int(input("Enter with a number: "))
contador = 1
cont=0
while contador <= number:
    result = number%contador
    if result == 0:
        cont+=1
    contador+=1
if cont == 2:
    message = "É um número primo!"
else:
    message = "Não é um número primo!"
