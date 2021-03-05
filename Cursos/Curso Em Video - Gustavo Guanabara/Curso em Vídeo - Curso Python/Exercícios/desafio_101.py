# Program: desafio_101.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 13:33

from datetime import date

def voto(idade):
    if idade > 0 and idade < 16:
        mensagem = 'Não pode votar!'
    elif (idade >= 16 and idade < 18) or (idade > 65):
        mensagem = 'Opcional'
    elif idade >= 18 and idade <= 65:
        mensagem = 'Obrigatório'
    else:
        mensagem = 'Você tem problemas mentais'
    return mensagem

def calculo(ano_nascimento):
    nascimento = ano_nascimento
    ano = date.today().year
    idade = 0
    if ano > nascimento:
        idade = ano - nascimento
    return idade

a_nascimento = int(input('Digite o seu ano de nascimento: '))
resposta = voto(calculo(a_nascimento))
print(resposta)