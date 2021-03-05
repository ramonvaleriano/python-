# Program: desafio_20.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 21:35

import random

def quantidade():
    q_alunos = int(input("Digite a quantidade de alunos: "))
    return q_alunos

def coleta(entrada):
    final = entrada()
    alunos = list()
    for e in range(final):
        aluno = str(input('Digite o nome do {}° aluno'.format(e+1)))
        alunos.append(aluno)
    return alunos

def embraralhando(colatados):
    mistura = random.shuffle(colatados(quantidade))
    return mistura

final = embraralhando(coleta)
print(final)