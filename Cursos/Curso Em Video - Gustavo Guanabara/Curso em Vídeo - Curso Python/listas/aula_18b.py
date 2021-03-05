# Program: aula_18b.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 08:52

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)