# Program: Listagem6_6.py
# Author: Ramon R. Valeriano
# Description:  
# Developed: 19/04/2020 - 13:09
# Updated:

notes = [0,0,0,0,0]
sum_ = 0
cont = 0

while cont<len(notes):
    notes[cont] = float(input("Enter with the note: "))
    sum_+=notes[cont]
    cont+=1
cont = 0
while cont<len(notes):
    print(notes[cont])
    cont+=1
media = sum_/cont
print("\n\n", media)
