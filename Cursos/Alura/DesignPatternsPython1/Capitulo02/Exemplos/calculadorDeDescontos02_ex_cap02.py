# Programa: calculadorDeDescontos02_ex_cap02.py
# Author: Ramon R. Valeriano
# Description: Modelo para apenas calculasr os descontos
# Developed: 17/04/2021 - 08:29
# Upadated:  21/04/2021 - 06:17
# Updated:   21/04/2021 - 06:30


from orcamento_ex_cap02 import Orcamento, Item
from desconto01_ex_cap02 import Desconto_por_cinco_itens, \
    Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos:

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
        ).calcula(orcamento)

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