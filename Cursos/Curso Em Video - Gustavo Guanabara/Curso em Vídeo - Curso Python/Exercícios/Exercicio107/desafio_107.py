# Program: desafio_112.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 09/10/2020 - 11:36

from Exercícios.Exercicio107 import moeda

preço = float(input('Digite o precço: '))
porcentagem = float(input('Digite o valor da porcentagem: '))

resultado1 = moeda.aumento(preço, porcentagem)
print(f'O valor da do produto: {preço}, a Porcentagem: {porcentagem}, '
      f'o Aumento: {resultado1}')

resultado2 = moeda.diminuir(preço, porcentagem)
print(f'O valor da do produto: {preço}, a Porcentagem: {porcentagem}, '
      f'a Diminuição: {resultado2}')

resultado3 = moeda.dobro(preço)
print(f'O preço: {preço}, o Dobro: {resultado3}')

resultado4 = moeda.metade(preço)
print(f'O preço: {preço}, a Metade: {resultado4}')
