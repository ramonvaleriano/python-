# Program: desafio_112.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/10/2020 - 11:37
# Updated: 09/10/2020 - 12:18

from Exercícios.Exercicio108 import moeda

preço = float(input('Digite o precço: '))
porcentagem = float(input('Digite o valor da porcentagem: '))

resultado1 = moeda.conversao(moeda.aumento(preço, porcentagem))
print(f'O valor da do produto: {moeda.conversao(preço)}, a Porcentagem: {porcentagem}%, '
      f'o Aumento: {resultado1}')

resultado2 = moeda.conversao(moeda.diminuir(preço, porcentagem))
print(f'O valor da do produto: {moeda.conversao(preço)}, a Porcentagem: {porcentagem}%, '
      f'a Diminuição: {resultado2}')

resultado3 = moeda.conversao(moeda.dobro(preço))
print(f'O preço: {moeda.conversao(preço)}, o Dobro: {resultado3}')

resultado4 = moeda.conversao(moeda.metade(preço))
print(f'O preço: {moeda.conversao(preço)}, a Metade: {resultado4}')
