# Program: calculadorDeImpostosCap03.py
# Author: Ramon R. Valeriano
# Description: Faremos os calculos de impostos aqui.
# Developed: 22/04/2021 - 08:36

from impostosCap03 import ISS, ICMS, ICPP, IKCV
from orcamentoCap03 import Item, Orcamento

class Calculador_de_impostos:

    def realiza_calcula(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        return imposto_calculado


if __name__ == '__main__':

    calculador = Calculador_de_impostos()
    orcamento = Orcamento()

    orcamento.adiciona_item(Item('ITEM - 1', 50))
    orcamento.adiciona_item(Item('ITEM - 1', 200))
    orcamento.adiciona_item(Item('ITEM - 1', 250))

    # ISS, ICMS
    resutado1 = calculador.realiza_calcula(orcamento, ISS())
    resutado2 = calculador.realiza_calcula(orcamento, ICMS())

    # ISS, ICMS
    resutado3 = calculador.realiza_calcula(orcamento, ICPP())
    resutado4 = calculador.realiza_calcula(orcamento, IKCV())

    print('ISS, ICMS')
    print(f'O imposto calculuado inicialmente(ISS) é R$ {resutado1}')
    print(f'O imposto calculuado inicialmente(ICMS) é R$ {resutado2}')

    print('ICPP, IKCV')
    print(f'O imposto calculuado inicialmente(ICPP) é R$ {resutado3}')
    print(f'O imposto calculuado inicialmente(IKCV) é R$ {resutado4}')

