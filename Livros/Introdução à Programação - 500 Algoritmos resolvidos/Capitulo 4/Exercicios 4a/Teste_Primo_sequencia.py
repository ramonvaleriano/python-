# Program: Teste_Primo_sequencia.py
# Author:
# Description:
# Developed:
# Updated:

number = int(input("Enter with a number: "))

cont = 0
for n in range(1, number+1):
    for e in range(1, number+1):
        if n%e==0:
            cont+=1
        if cont == 2:
            print(n, end=" ")   

