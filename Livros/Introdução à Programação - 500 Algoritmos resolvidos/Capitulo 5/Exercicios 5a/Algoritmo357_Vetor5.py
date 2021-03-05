# Program: Algoritmo357_Vetor5.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 15:48
# Updated:

lista = list()
people = 2

for e in range(people):
    dados = []
    name = str(input("Enter with %d° name: " %(e+1)))
    name = name.upper()
    dados.append(name)
    salary = float(input("Enter with %d° salary: " %(e+1)))
    result = salary + ((salary*8)/100)
    dados.append(result)
    lista.append(dados)
print()
cont = 0
for i, v in enumerate(lista):
    print("%d - %12s - R$%5.2f" %((i+1), v[cont], v[cont+1]))
