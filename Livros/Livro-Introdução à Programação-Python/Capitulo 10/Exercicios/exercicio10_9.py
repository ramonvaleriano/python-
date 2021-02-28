# Program: exercicio10_9.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 24/02/2020 - 21:59

class Cidade:
    def __init__(self, nome, populacao):
        self._nome = nome.title()
        self._populacao = populacao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        return self._nome

    @property
    def populacao(self):
        return self._populacao

    @populacao.setter
    def populacao(self, novo_numero):
        self._populacao = novo_numero
        return self._populacao

    def __str__(self):
        return f'{self.nome} e sua Populção é de {self.populacao}'


class Estado:
    def __init__(self, nome, cidades):
        self._nome = nome
        self._cidades = cidades

    def __getitem__(self, item):
        return self._cidades[item]

    def __str__(self):
        return f'Estado {self.nome}'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        return self._nome

    def adicionar_cidade(self, nova_cidade):
        self._cidades.append(nova_cidade)










petrolina = Cidade('Petrolina', 300000)
juazeiro = Cidade('Juazeiro', 200000)
bonfim = Cidade('Bondim', 150000)
jacobina = Cidade('Jacobina', 100000)

bahia = Estado('Bahia', [juazeiro, bonfim])
print(bahia)

for i in bahia:
    print(i)

bahia.adicionar_cidade(jacobina)

for i in bahia:
    print(i)