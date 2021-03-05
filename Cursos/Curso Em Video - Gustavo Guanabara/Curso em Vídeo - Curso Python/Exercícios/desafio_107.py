# Program: desafio_112.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 09/10/2020 - 11:14

import moeda

numero = float(input('Digite um número desejado: '))
porcentagem = float(input('Qual aumento você quer dar: '))
resultado1 = moeda.aumentar(numero, porcentagem)
print(f'O valor digitado: {numero}, o Aumento {porcentagem}%, o Aumento: {resultado1}')
resultado2 = moeda.diminuir(numero, porcentagem)
print(f'O valor digitado: {numero}, o Retirada {porcentagem}%, a Diminuição: {resultado2}')
resultado3 = moeda.dobrar(numero)
resultado4 = moeda.metade(numero)
print(f'O dobro do número: {numero} = {resultado3}')
print(f'O triplo do número: {numero} = {resultado4}')