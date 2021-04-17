# Program: calculadorDeImpostos.py
# Author: Ramon R. Valeriano
# Description: Faremos os calculos de impostos aqui.
# Developed: 16/04/2021 - 21:33

from impostos import ISS, ICMS
from orcamento import Orcamento

class Calculador_de_impostos:

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calculo(orcamento)

        return imposto_calculado

if __name__ == '__main__':

    orcamento = Orcamento(500)
    calculador = Calculador_de_impostos()

    print(f'Valor do imposto ISS R$ {calculador.realiza_calculo(orcamento, ISS())}')
    print(f'Valor do imposto ISS R$ {calculador.realiza_calculo(orcamento, ICMS())}')
