# Program: desafio_031.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:33

distancia = float(input('Calcule a distancia Percorrida: '))
if distancia>0 and distancia<=200:
    valor = 0.50 * distancia
elif distancia>200:
    valor= 0.45 * distancia
else:
    valor = 0
print(valor)