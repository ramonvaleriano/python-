# Program: Algoritmo210_Para36.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 17:26
# Updated:

previous = int(input("Enter with the firt number: "))
current = int(input("Enter with the second number: "))
result = 0
print(previous)
print(current)
for e in range(8):
    if current%2==0:
        result = current - previous
    else:
        result = current + previous
    previous = current
    current = result
    print(result)
