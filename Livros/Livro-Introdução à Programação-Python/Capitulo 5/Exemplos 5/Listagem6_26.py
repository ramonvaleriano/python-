# Program: Listagem6_26.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 16:02
# Updated:

l = [6, 7, 9, 10, 12]
number = int(input("Entre com um número para fazermos um busca: "))
for e in l:
    if number == e:
        print(number)
        print("Elementro encontrado")
        break
else:
    print("Elemento não encontrado!")
