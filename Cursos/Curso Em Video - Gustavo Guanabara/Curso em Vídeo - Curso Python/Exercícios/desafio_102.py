# Program: desafio_102.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 13:56


def fatorial(num=1, show = True):
    """
    -> Rotina fatorial para fazer com que o ocorra o fatorial
    :param num: o número que e passado para ser o fatorial
    :param show: Variável que decide se será mostrado todo o calulo na tela
    :return: f
    """
    f = 1
    for c in range(num, 0, -1):
        f*=c
        if show:
            print(f'{c}', end=' ')
    return f
help(fatorial)
resultado = fatorial(5)
print(resultado)
resultado = fatorial(6, False)
print(resultado)
