# Program: aula_19c.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 06/10/2020 - 16:56

filmes = {'Título':'Stars Wars',
          'Ano':1977,
          'Diretor':'Geoger Lucas'
         }

for chaves, valores in filmes.items():
    print(f'O {chaves} é: {valores}')