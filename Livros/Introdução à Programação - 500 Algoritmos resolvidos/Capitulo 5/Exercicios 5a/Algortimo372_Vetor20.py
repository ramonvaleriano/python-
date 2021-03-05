# Program: Algortimo372_Vetor20.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/05/2020 - 21:34
# Updated:

tabela = list()
quantity = 12

for e in range(quantity):
    team = str(input("Enter with the %d° Team: " %(e+1)))
    tabela.append(team)
print("\n\n")
for i, v in enumerate(tabela):
    print("%02d - %-12s" %(i, v))
print("\n\n")

quantity = len(tabela)
cont = 0
for n in range(quantity):
    for g in range((n+1), quantity):
        print("%+12s x %-12s" %(tabela[n],tabela[g]))
    
