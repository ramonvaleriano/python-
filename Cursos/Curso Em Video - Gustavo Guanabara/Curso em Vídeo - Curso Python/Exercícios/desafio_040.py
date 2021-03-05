# Program: desafio_040.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 18:49

nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))

if nota1 >= 0 and nota2 >= 0 and nota2<=10 and nota1<=10:
    media = (nota2+nota1)/2
    if media>=7:
        print('Aluno aprovado por média!')
    elif media>=5 and media<7:
        print('Aluno em recuperação!')
    else:
        print('Aluno reprovado!')
else:
    print('Impossível')