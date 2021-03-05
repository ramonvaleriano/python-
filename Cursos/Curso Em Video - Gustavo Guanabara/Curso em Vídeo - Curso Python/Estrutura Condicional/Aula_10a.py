# Program: Aula_10a.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 10:50

tempo_carro = int(input('Digite quantos anos tem o seu carro: '))
if tempo_carro>0:
    if tempo_carro<=3:
        print('Seu carro é novo!')
    else:
        print('Seu carro é velhinho!')
else:
    print('Você tem problemas mentais, precisa se tratar!')