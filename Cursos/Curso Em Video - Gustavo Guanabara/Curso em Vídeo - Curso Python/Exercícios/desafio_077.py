# Program: desafio_077.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 23:32

palavras = 'Buceta', 'Xoxota', 'Anus', 'Cu', 'Priquito'
quantidade = len(palavras)

for x, e in enumerate(palavras):
    print(x+1)
    for i in e:
        if (i in 'aeiou')or(i in 'AEIOU'):
            print(i, end=' ')
    print()