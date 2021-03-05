# Program: desafio_090.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 08:29

aluno = dict()
nome = str(input('Digite o o nome do aluno: '))
aluno['nome'] = nome
media = float(input('Digite a media do aluno: '))
if media >=0 and media <=5:
    situacao = 'Reprovado'
elif media > 5 and media < 7:
    situacao = 'Recuperação'
elif media >=7 and media<=10:
    situacao = 'Aprovado'
else:
    situcao = 'Não existe!'
aluno['media'] = media
aluno['situacao'] = situacao
for chave, elementos in aluno.items():
    print(f'{chave.title()} = {elementos}')