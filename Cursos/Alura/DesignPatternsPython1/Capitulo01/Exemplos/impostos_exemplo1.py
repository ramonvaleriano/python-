# Program: impostos_exemplo1.py
# Author: Ramon R. Valeriano
# Description: Todas as funções, metodos para se calculos os impostos
# Developed: 16/04/2021 - 21:13
# Updated:   16/04/2021 - 21:23 - Vamos deixar nossos orientado a objetos

class ISS:

    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ICMS:

    def calcula(self, orcamento):
        return orcamento.valor * 0.06
