# Program: Ex002.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 13/09/2020 - 15:19

def entrada():
    name = str(input(('Digite seu nome: ')))
    return name

def mensagem(i_funcao):
    word = i_funcao()
    print('Bem vindo %s' %word)

# palavra = entrada()
mensagem(entrada)
print('Testando format {}'.format("Aparece Caralho!"))


