# Program: Listagem6_5.py
# Author: Ramon R. Valeriano
# Description: Calculando a Média 
# Developed: 19/04/2020 - 13:02
# Updated:

notes = [6, 7, 5, 8, 9]
sum_ = 0
cont = 0

while cont<5:
    sum_+=notes[cont]
    cont+=1
media = sum_/cont
print(media)
