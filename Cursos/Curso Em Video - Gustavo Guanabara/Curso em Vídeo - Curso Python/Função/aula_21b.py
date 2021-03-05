# Program: aula_21b.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 07/10/2020 - 21:54

def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param inicio: Parâmetro que dará incio a contagem
    :param fim: Parâmetro final da contagem
    :param passo: A quantos números irá pular, saltar.
    :return: Sem retorno, apenas exibe dados.
    """
    c = inicio
    while c<=fim:
        print(f'{c}', end=' ')
        c+=passo
    print('\nFim!')

contador(2, 10, 2)
help(contador)