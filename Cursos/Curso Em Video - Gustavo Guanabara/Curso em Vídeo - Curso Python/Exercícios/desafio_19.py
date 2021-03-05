# Program: desafio_19.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 21:20

import random

def quantidade():
    q_alunos = int(input('Digite a quantidade de alunos: '))
    return q_alunos

def nomes(entrando):
    final = (entrando())
    turma = list()
    for e in range(final):
        aluno = str(input('Digite o nome {}° aluno'.format((e+1))))
        turma.append(aluno)
    return turma

def sorteio(cambada):
    sorteado = random.sample(cambada(quantidade), 1)
    return sorteado

final = sorteio(nomes)
print(final)