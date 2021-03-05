# Program: aula_19d.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 06/10/2020 - 17:02

locadora = list()

filme = {'Título':'Stars Wars',
          'Ano':1977,
          'Diretor':'Geoger Lucas'
         }

locadora.append(filme)
filme = {'Título':'Jhon Wick',
          'Ano':2016,
          'Diretor':'Os Irmãos Russos.'
         }
locadora.append(filme)
filme = {'Título':'Matrix',
          'Ano':1999,
          'Diretor':'Os Irmãos Russos.'
         }
locadora.append(filme)

print(locadora)
print(locadora[0]['Ano'])
print(locadora[2]['Título'])