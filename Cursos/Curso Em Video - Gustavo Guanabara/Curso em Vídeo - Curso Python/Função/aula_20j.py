# Program: aula_20j.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 13:15

def dobra(lista):
    pos = 0
    while pos<len(lista):
        lista[pos]*=2
        pos+=1



# Programa Principal
valores = [2, 5, 1, 8, 2, 9]
dobra(valores)
numeros_demais = [1,6,2,8,3,6,7,1,6,2,]
dobra(numeros_demais)
print(valores)
print(numeros_demais)
