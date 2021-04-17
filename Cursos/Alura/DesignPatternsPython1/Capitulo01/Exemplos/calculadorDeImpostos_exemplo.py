# Program: calculadorDeImpostos_exemplo.py
# Author: Ramon R. Valeriano
# Description: Faremos os calculos de impostos aqui.
# Developed: 16/04/2021 - 20:59

from impostos_exemplo import calculo_ISS, calculo_ICMS

class Calculador_de_impostos:

    def realiza_calcula(self, orcamento, imposto):
        if imposto == 'ISS':
            imposto_calculado = calculo_ISS(orcamento)

        if imposto == 'ICMS':
            imposto_calculado = calculo_ICMS(orcamento)

        return imposto_calculado

if __name__ == '__main__':
     from orcamento_exemplo import Orcamento

     calculador = Calculador_de_impostos()
     orcamento = Orcamento(500)

     resutado1 = calculador.realiza_calcula(orcamento, 'ISS')
     resutado2 = calculador.realiza_calcula(orcamento, 'ICMS')

     print(f'O imposto calculuado inicialmente(ISS) é R$ {resutado1}')
     print(f'O imposto calculuado inicialmente(ICMS) é R$ {resutado2}')