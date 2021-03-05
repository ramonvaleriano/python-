# Program: Algoritmo127_se38.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 10:40
# Updated:

name = input("Enter with your name: ")
note1 = float(input("Enter with your firt note: "))
note2 = float(input("Enter with your second note: "))

media = (note1+note2)/2

if media >= 7:
    message = "Accept!"
elif(media>=3)and(media<7):
    message = "Retake Test!"
else:
    message = "Denied!"
print(name)
print(media)
print(message)
