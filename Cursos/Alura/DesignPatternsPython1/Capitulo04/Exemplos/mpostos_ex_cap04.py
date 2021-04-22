# Program: impostos_ex_cap03.py
# Author: Ramon R. Valeriano
# Description: Todas as funções, metodos para se calculos os impostos
# Developed: 21/04/2021 - 07:15
# Updated:   21/04/2021 - 07:38
# Updated:   22/04/2021 - 08:52

from abc import ABCMeta, abstractmethod

class Imposto:

    def __init__(self, outro_imposto):
        self.outro_imposto = outro_imposto

    def calcula(self, orcamento):
        pass

class Template_de_imposto_condicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICPP(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        if orcamento.valor > 500:
            return True
        else:
            return False

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07


class IKCV(Template_de_imposto_condicional):

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.itens:
            if item > 100:
                return True
        else:
            return False

    def deve_usar_maxima_taxacao(self, orcamento):
        if (orcamento.valor > 500 and
                self.__tem_item_maior_que_100_reais(orcamento)):
            return True
        else:
            return False

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06



