# Programa: calculadorDeDescontos_ex_cap02.py
# Author: Ramon R. Valeriano
# Description: Modelo para apenas calculasr os descontos
# Developed: 17/04/2021 - 08:29

from orcamento_ex_cap02 import Orcamento, Item

class Calculador_de_descontos:

    def calcula(self, orcamento):

        if orcamento.total_itens > 5:
            desconto = orcamento.valor * 0.1

            return desconto

        elif orcamento.valor > 500:
            desconto = orcamento.valor * 0.07

            return desconto

        else:
            desconto = orcamento.valor

            return desconto


if __name__ == '__main__':

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    valor_total = orcamento.valor

    print(f'Nosso valor total acumulado é R$ {valor_total}')

    calculador = Calculador_de_descontos()

    desconto = calculador.calcula(orcamento)

    print(f'O desconto gerado foi de: R$ {desconto:0.2f}')