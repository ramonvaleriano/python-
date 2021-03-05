# Program: desafio_053.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 28/09/2020 - 20:56

frase = str(input('Digite uma frase para que nós posssamo verificar se ela é um palíndromo ou não: '))
composicao = frase.split()
parte1 = composicao[0]
parte2 = composicao[-1]
inversao1 = parte1[::-1]
inversao2 = parte2[::-1]
if parte1==inversao2 and parte2==inversao1:
    print('Essa frase é um políndromo!')
else:
    print('Não é não!')