# Program: desafio_036.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 17:19

def dividindo_valor(casa, anos):
    valor_prestacao = ((casa/anos)/12)
    return valor_prestacao

def porcentagem(salario):
    new_salario = ((salario*30)/100)
    return new_salario

def test(casa, anos, salario, f_divisao, f_prestacao):
    if f_prestacao(salario) <= dividindo_valor(casa, anos):
        print('Emprestimo será aceito!')
    else:
        print('Emprestimo Negado!')

salario = float(input('Digite o valor de seu salario: '))
casa = float(input('Digite o valor da casa: '))
anos = int(input('Digite o valor dos anos: '))

test(casa, anos, salario, dividindo_valor, porcentagem)