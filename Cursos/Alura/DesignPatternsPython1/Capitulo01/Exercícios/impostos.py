# Program: impostos.py
# Author: Ramon R. Valeriano
# Description: Todas as funções, metodos para se calculos os impostos
# Developed: 16/04/2021 - 21:31

class ISS:

    def calculo(self, orcamento):
        return orcamento.valor * 0.1

class ICMS:

    def calculo(self, orcamento):
        return orcamento.valor * 0.06