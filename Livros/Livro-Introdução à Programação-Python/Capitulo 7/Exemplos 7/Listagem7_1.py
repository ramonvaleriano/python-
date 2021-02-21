# Program: Listagem7_1.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 16:45
# Updated:

s = "Olá Mundo"
print(s)
s = list(s)
print(s)
s[0] = "a"
s="".join(s)
print(s)
s = list(s)
s[0]="o"
s="".join(s)
print(s)
