# Programa: descontos_ex_cap02.py
# Author: Ramon R. Valeriano
# Description: Todas as metricas de desconto estarão aqui
# Developed: 21/04/2021 - 06:12

class Desconto_por_cinco_itens:

    def calcula(self, orcamento):

        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return 0

class Desconto_por_mais_de_quinhentos_reais:


    def calcula(self, orcamento):

        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return 0
