# Program: desafio_053Pelo_professor.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 07:12

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for e in range(len(junto)-1, -1, -1):
    inverso+=junto[e]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palindromo!')
