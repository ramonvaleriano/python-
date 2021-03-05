# Program: desafio_089.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 11:35

""" Coleta de dados:"""
sala_aula = list()
option = 'S'
while True:
    dados = list()
    if len(sala_aula)==0 or option == 'S':
        name = str(input('Digite o nome do aluno: ')).strip().upper()
        dados.append(name)
        nota1 = float(input(f'Digite a primeira nota de {name}: '))
        nota2 = float(input(f'Digite a segunda nota de {name}: '))
        dados.append(nota1)
        dados.append(nota2)
        media = (nota1+nota2)
        dados.append(media)
        sala_aula.append(dados[:])
        dados.clear()
    elif option == 'N':
        print('Fim da coleta de dados!')
        break
    else:
        print('Opção Invalida!')
    option = str(input('Digite a opção desejada[S/N]: ')).strip().upper()[0]

""" Visualizando os dados: """

for coletados in sala_aula:
    print(f'Nome: {coletados[0]:^20} >> Nota 1 {coletados[1]:^5.2f} >> Nota2 {coletados[2]:^5.2f} >>  Media {coletados[3]:^5.2f}')



