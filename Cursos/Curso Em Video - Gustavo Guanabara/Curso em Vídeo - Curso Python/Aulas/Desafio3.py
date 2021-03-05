# Program: Desafio3.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 13/09/2020 - 12:36


def dados_pessoais():
    lista = list()
    day = int(input("Digite o dia de seu nascimento: "))
    lista.append(day)
    month = int(input("Digite o mês do seu ano: "))
    lista.append(month)
    year = int(input("Digite o ano de seu ano: "))
    lista.append(year)
    return lista

def mensagem(funcao):
    lista1 = funcao()
    print(f'{lista1[0]}, {lista1[1]}, {lista1[2]}')


dados_pessoais()
mensagem(dados_pessoais)
