# Program: desafio_103.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 14:41

CONT = 0

def ficha(nome = "Jogardor", gols=0):
    """
    -> Função desenvolvida para criar um ficah ríída para um jogador
    :param nome: O nome do jogador, que tem um variável pré-definida
    :param gols: Variável para denominar a quantidade de gols, caso não recebe 0
    :return: Não retorna nada.
    """
    global CONT
    CONT+=1
    print(f'Jogador: {nome:10}, Gols: {gols:5}, Resgistro: {cont:05}')

ficha("Ramon")
ficha("Milla", 5)
ficha("Gale", 30)
ficha(gols=1)

    
