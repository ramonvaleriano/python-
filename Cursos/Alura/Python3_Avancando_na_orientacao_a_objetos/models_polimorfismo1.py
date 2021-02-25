class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super(Serie, self).__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('Vigadores - Guerra Infinita', 2018, 160)
atlanta = Serie('Atlatan', 2018, 2)

filmes_e_series = [vingadores, atlanta]

for dados in filmes_e_series:
    detalhes = dados.duracao if hasattr(dados, 'duracao') else dados.temporadas
    print(f'{dados.nome} - {detalhes} - {dados.likes}')

