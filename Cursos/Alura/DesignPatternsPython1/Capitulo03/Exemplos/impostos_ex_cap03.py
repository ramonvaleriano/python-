# Program: impostos_ex_cap03.py
# Author: Ramon R. Valeriano
# Description: Todas as funções, metodos para se calculos os impostos
# Developed: 21/04/2021 - 07:15

class ISS:

    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ICMS:

    def calcula(self, orcamento):
        return orcamento.valor * 0.06

class ICPP:

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return orcamento.valor * 0.05

class IKCV:

    def calcula(self, orcamento):
        if (orcamento.valor > 500 and
                self.__tem_item_maior_que_100_reais(orcamento)):
            return orcamento.valor * 0.1
        else:
            return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.itens:
            if item > 100:
                return True
        return False