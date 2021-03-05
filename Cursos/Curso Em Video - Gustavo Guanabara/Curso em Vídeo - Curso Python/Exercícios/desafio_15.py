# Programa: desafio_15.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 23/09/2020 - 21:45

def valor(dias, km):
    q_km = km*0.15
    q_dias = dias*60
    total = q_km + q_dias
    return total

dias = int(input('Qual a quantidade de dias? '))
km = float(input('Qual a KM? '))
print(valor(dias, km))