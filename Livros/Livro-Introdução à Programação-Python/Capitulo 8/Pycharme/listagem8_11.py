# Program: listagem8_11.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 16/09/2020 - 06:37

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*fatorial(n-1))

print(fatorial(4))
print(fatorial(6))
print(fatorial(3))
