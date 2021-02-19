# Program: cliente.py
# Author: Ramon R. Valeriano
# Description: Modulo desenvolvido para que pudessemos ter acesso ao uma nova classe cliente, que irá nos auxiliar em
#              em outro modulos.
# Developed: 19/02/2020 - 15:16

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @proprty nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando Setter nome()")
        self.__nome = nome


nome_teste = Cliente('ramon')
print(nome_teste.nome)
nome_teste.nome = 'milla'
print(nome_teste.nome)