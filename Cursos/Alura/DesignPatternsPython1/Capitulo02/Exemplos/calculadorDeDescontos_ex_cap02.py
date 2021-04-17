# Programa: calculadorDeDescontos_ex_cap02.py
# Author: Ramon R. Valeriano
# Description: Modelo para apenas calculasr os descontos
# Developed: 17/04/2021 - 08:29

from orcamento_ex_cap02 import Ocamento, Item

class Calculador_de_descontos:

    def calcula(self, orcamento):

        if orcamento.total_itens > 5:
            desconto = orcamento.valor * 0.1

            return desconto

        elif orcamento.total_itens > 500:
            desconto = orcamento.valor * 0.07

            return desconto

if __name__ == '__main__':

    orcamento = Ocamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    valor_total = orcamento.valor

    print(f'Nosso valor total acumulado é R$ {valor_total}')