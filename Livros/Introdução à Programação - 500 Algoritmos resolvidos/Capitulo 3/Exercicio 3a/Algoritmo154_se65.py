# Program: Algoritmo154_se65.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 13:51
# Updated:

board = input("Enter with the your board: ")
number = int(board[-1])
test = type(number) is int
#print(test)
print(number)
#vid = board[-1]
#print(vid)
if(number>=0)and(number<10)and(test == True):
    if number == 1:
        message = "Janeiro"
    elif number == 2:
        message = "Fevereiro"
    elif number == 3:
        message = "Março"
    elif number == 4:
        message = "Abril"
    elif number == 5:
        message = "Maio"
    elif number == 6:
        message = "Junho"
    elif number == 7:
        message = "Julho"
    elif number == 8:
        message = "Agosto"
    elif number == 9:
        message = "Setembro"
    elif number == 0:
        message = "Outubro"
    else:
        message = "Porra nenhuma!"
else:
    message = "Dou are you crazy?"

print(message)
