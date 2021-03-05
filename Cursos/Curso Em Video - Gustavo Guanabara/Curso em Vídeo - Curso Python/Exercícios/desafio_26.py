# Program: desafio_26.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 10:07

def contador(n_nome):
    quantidade = n_nome.upper().count('A')
    return quantidade

def localizador(n_nome):
    p = 0
    lista_posições = list()
    while p>-1:
        p = n_nome.upper().find('A', p)
        if p>=0:
            lista_posições.append(p)
            p+=1
    return lista_posições

def primeiro(f_locaizador, n_nome):
    completo = f_locaizador(n_nome)
    first = completo[0]
    return first

def ultimo(f_localizador, n_nome):
    completo = f_localizador(n_nome)
    last = completo[-1]
    return last

nome = str(input('Digite o seu nome completo: '))
numero = contador(nome)
print('{} é a quantidade de vezes que aparece a letra A'.format(numero))
n_first = primeiro(localizador, nome)
print(n_first)
n_last = ultimo(localizador, nome)
print(n_last)
