# Program: aula_16f.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 20:19

a = (2, 5, 4)
b = 5, 8, 1, 2
c = a + b
print(c)
n = 4
print(f'Quantas vezes se repeti o número:{n} -->> {c.count(n)} vezes')
print(f'A posição do elemento primeiro :{n} ==>> {c.index(n)}')
print(c.index(5, 2))