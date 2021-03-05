# Programa: Algoritmo138_se49.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 14:01
# Updated:

number = int(input("Enter with a number: "))

if(type(number) is int)and(number>0):
    if number == 1:
        message = "Janeiro!"
    elif number == 2:
        message = "Fevereiro!"
    elif number == 3:
        message = "Março!"
    elif number == 4:
        message = "Abril"
    elif number == 5:
        message = "Maio"
    elif number == 6:
        message = "Junho!"
    elif number == 7:
        message = "Julho!"
    elif number == 8:
        message = "Agosto!"
    elif number == 9:
        message = "Setembro!"
    elif number == 10:
        message = "Outubro!"
    elif number == 11:
        message = "Novembro!"
    elif number == 12:
        message = "Dezembro!"
    else:
        message = "You are asshole!"
else:
    message = "What fuck is this?!"

print(message)
