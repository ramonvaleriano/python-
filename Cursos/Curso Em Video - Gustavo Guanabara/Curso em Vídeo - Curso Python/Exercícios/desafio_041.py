# Program: desafio_041.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 18:54

import datetime

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano = datetime.date.today()
if ano_nascimento>0:
    idade = ano.year - ano_nascimento
    if idade>=0 and idade<9:
        print('Mirim')
    elif idade>=9 and idade<14:
        print('Infantil')
    elif idade>=14 and idade<19:
        print('Junior')
    elif idade>=19 and idade<20:
        print('Sênior')
    else:
        print('Master!')
else:
    print('Não há como!')