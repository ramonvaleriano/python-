# Programa: calculadorDeDescontosCap02.py
# Author: Ramon R. Valeriano
# Description: Modelo para apenas calculasr os descontos
# Developed: 21/04/2021 - 06:50

from orcamentoCap02 import Item, Orcamento
from descontoCap02 import Sem_desconto, Desconto_por_cinco_itens, \
    Desconto_por_mais_de_quinhentos_reais

class Calculador_de_descontos:

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto)
        ).calcula(orcamento)

        return desconto

if __name__ == '__main__':

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    valorTotal = orcamento.valor

    print(f'O valor total dos itens é de R$ {valorTotal}')

    desconto = Calculador_de_descontos().calcula(orcamento)

    print(f'O desconto calculado foi de R$ {desconto:0.2f}')