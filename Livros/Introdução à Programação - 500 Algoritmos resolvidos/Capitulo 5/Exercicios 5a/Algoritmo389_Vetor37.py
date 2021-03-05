# Program: Algoritmo389_Vetor37.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/05/2020 - 22:21
# Updated:

quantity = 12
meses = list()
for e in range(quantity):
    temperatura = float(input("Entre com a temperatura do mês %d: " %(e+1)))
    meses.append(temperatura)
    if e == 0 :
        maior = temperatura
        menor = temperatura

    if temperatura > maior:
        maior = temperatura
        m = e
    if temperatura < menor:
        menor = temperatura
        n = e
print(maior, m+1)
print(menor, n+1)
    
