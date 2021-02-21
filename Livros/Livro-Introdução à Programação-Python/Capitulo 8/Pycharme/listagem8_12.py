# Program: listagem8_12.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 16/09/2020 - 06:44

def fatorial(n):
    print('Calculando o fatorial de %d' %n)
    if n == 0 or n == 1:
        print('Fatorial de %d = 1' %n)
        return 1

    else:
        fat = n*fatorial(n-1)
        print('Fatorial de %d = %d' %(n, fat))
        return fat

fatorial(4)
#fatorial(2)
#fatorial(3)
