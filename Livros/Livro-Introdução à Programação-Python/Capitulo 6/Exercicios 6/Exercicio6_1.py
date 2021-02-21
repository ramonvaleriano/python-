# Program: Exercicio6_1.py
# Author: Ramon R. Valeriano
# Description:  
# Developed: 19/04/2020 - 13:21
# Updated:

notes = [0,0,0,0,0,0,0]
sum_ = 0
quantity = len(notes)
cont = 0
for x, e in enumerate(notes):
    notes[x] = float(input("Enter with the %d° note: " %(x+1)))
    sum_+=notes[x]
print(notes)
for x,e in enumerate(notes):
    print("%d° -> %3.2f" %((x+1), e))
media = sum_/quantity
print("\n\n", media)
