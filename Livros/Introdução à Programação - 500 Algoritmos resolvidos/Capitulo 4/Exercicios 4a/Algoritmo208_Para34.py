# Program: Algoritmo208_Para34.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 16:59
# Updated:

anterior = 0
atual = 1

for e in range(11):
    sum_ = anterior + atual
    anterior = atual
    atual = sum_
    
    print(sum_)
