# Program: Listagem8_10.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 13:15
# Updated:

def fatorial(number):
    fat = 1
    x = 1
    while x<=number:
        fat*=x
        x+=1
    return fat

number1 = int(input("Digite o número que deseja obter o fatorial: "))
result = fatorial(number1)
print(result)
