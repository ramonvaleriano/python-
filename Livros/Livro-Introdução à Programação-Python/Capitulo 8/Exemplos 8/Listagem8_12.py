# Program: Listagem8_12.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 15:54
# Updated:

def fatorial(n):
    print("Calculando o fatorial de %d" %n)
    if n == 0 or n == 1:
        print("Fatorial de 1 = %d" %(n))
        return 1
    else:
        fat = n*fatorial(n-1)
        print("Fatorial de %d = %d" %(n, fat))
    return fat
print(fatorial(4))
