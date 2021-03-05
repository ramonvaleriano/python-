# Program: desafio_105.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 16:57

def notas(*todas):
    todas_notas = dict()
    todas_notas['Quantidade'] = (len(todas))
    todas_notas['Maior Nota'] = (max(todas))
    todas_notas['Menor Nota'] = (min(todas))
    media = ((sum(todas))/(len(todas)))
    todas_notas['Media da Turma'] = media
    situacao = 'Aprovado' if media >= 7 else 'Reprovado'
    todas_notas['Situação'] = situacao
    return todas_notas
resultado = notas(7,1,9,2,0,7,5,6.7)
print(resultado)
