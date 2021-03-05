# Program: Algoritmo209_Para35.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 16:59
# Updated:

anterior = int(input("Enter with the firt number: "))
atual = int(input("Enter with the second number: "))
soma = anterior+atual
quantity = int(input("Enter with the quantity of number: "))
if atual>=anterior and quantity>=3:
    print(anterior)
    print(atual)
    for e in range(quantity-2):
        print(soma)
        anterior = atual
        atual = soma
        soma = anterior + atual
    
