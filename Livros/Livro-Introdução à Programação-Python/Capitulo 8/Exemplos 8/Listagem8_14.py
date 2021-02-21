# Program: Listagem8_14.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 16:01
# Updated:

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
