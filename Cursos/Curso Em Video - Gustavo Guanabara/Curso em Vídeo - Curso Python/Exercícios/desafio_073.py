# Program: desafio_073.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 21:48

tabela_brasileirao = ('Atletico-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco da Gama', 'Flamengo', 'Fluminense',
                      'Sport Recife', 'Santos', 'Fortaleza', 'Atletico-PR', 'Ceará', 'Atletico-GO', 'Corinthians',
                      'Grêmio', 'Coritiba', 'Bragantino', 'Botafogo', 'Goiás')
print(len(tabela_brasileirao))
for posicao, time in enumerate(tabela_brasileirao):
    print(f'{posicao+1} -->> {time}')
    if posicao == 4:
        break
os_quatro_ultimos = tabela_brasileirao[len(tabela_brasileirao)-1:15:-1]
#print(os_quatro_ultimos)

print('\nOs 4 ultimos colocados.')
for posicao, time in enumerate(tabela_brasileirao):
    if posicao>=15:
        print(f'{posicao+1} -->> {time}')

lista_alfabetica = sorted(tabela_brasileirao)
print('\nTimes em ordem alfabetica!')
for posicao, time in enumerate(lista_alfabetica):
    print(f'{time}->', end='')
print()

resposta = 'Chapecoence' in tabela_brasileirao
print(resposta)
if resposta:
    print(tabela_brasileirao.index('Chapecoence'))
else:
    print('Time não está na Série A!')

