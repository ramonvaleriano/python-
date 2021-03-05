# Program: aula_21c.py
# Author: Ramon R. Valeriano
# Upadated: 07/10/2020 - 22:09
# Description:

def soma(a=0, b=0, c=0):
    """
    -> Função responsável por somar números
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return: Sem retorno, apenas exibe o resutlado
    """
    s = a+b+c
    print(s)


soma(4,2,5)
soma(8, 1)
soma()
print()
help(soma)