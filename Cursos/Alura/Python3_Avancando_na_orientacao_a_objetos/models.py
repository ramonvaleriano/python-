class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme("Vigandors", "2017","3 horas")
print(vingadores.ano)
print(vingadores.nome)
print(vingadores.duracao)
print('\n')

atlanta = Serie('Atlanta', 2017, 2)
print(atlanta.nome)
print(atlanta.temporadas)
print(atlanta.ano)