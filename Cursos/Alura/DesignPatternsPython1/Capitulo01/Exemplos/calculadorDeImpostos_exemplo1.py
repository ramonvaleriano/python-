# Program: calculadorDeImpostos_exemplo.py
# Author: Ramon R. Valeriano
# Description: Faremos os calculos de impostos aqui.
# Developed: 16/04/2021 - 20:59
# updated:   16/04/2021 - 21:20 - Passando a função como parametro.

from impostos_exemplo1 import ISS, ICMS

class Calculador_de_impostos:

    def realiza_calcula(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        return imposto_calculado

if __name__ == '__main__':
     from orcamento_exemplo import Orcamento

     calculador = Calculador_de_impostos()
     orcamento = Orcamento(500)

     resutado1 = calculador.realiza_calcula(orcamento, ISS())
     resutado2 = calculador.realiza_calcula(orcamento, ICMS())

     print(f'O imposto calculuado inicialmente(ISS) é R$ {resutado1}')
     print(f'O imposto calculuado inicialmente(ICMS) é R$ {resutado2}')