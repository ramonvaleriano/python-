# Programa: descontos01_ex_cap02.py
# Author: Ramon R. Valeriano
# Description: Todas as metricas de desconto estarão aqui
# Developed: 21/04/2021 - 06:12
# Updated:   21/04/2021 - 06:25

class Desconto_por_cinco_itens:

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class Desconto_por_mais_de_quinhentos_reais:

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)

class Sem_desconto:

    def calcula(self):
        return 0