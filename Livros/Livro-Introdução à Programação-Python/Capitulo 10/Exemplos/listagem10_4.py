# Program: listagem10_4.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 24/02/2020 - 09:05

class Cliente:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
        return self.__telefone


valeriano = Cliente("Ramon R. Valeriano", "071992774903")
grabriela = Cliente("Milla Gabriela Valeriano", "1234567890")

print(valeriano.nome)
print(valeriano.telefone)

print(grabriela.nome)
print(grabriela.telefone)
