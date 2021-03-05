# Program: desafio_039.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 18:02

import datetime

ano_nascimento = int(input('digite o ano de nascimento '))

ano = datetime.date.today()
#print(ano.year)
idade = ano.year - ano_nascimento
if idade>0 and idade<18:
    faltam = 18 - idade
    print('Ainda vai se Alsitar!')
    print('Faltam {} anos para você se alistar!'.format(faltam))
elif idade == 18:
    print('É a hora de se alistar!')
elif idade>18:
    passou = idade - 18
    print('Pasou da hora de se alistar!')
    print('Se passaram {} anos da epoca de se alistar'.format(passou))
else:
    print('Que tipo de idade é essa?')