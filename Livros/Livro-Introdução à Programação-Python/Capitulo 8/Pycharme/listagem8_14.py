# Program: listagem8_14.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 16/09/2020 - 06:51

def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(4))