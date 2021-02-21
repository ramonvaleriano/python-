# Program: Listagem8_11.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 15:51
# Updated:

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)
print(fatorial(4))
