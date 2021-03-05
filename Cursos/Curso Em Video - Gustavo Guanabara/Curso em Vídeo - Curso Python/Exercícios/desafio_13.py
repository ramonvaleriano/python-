# Programa: desafio_13.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 23:05

def entrada():
    salario = float(input("Digite o valor do salario: "))
    return salario

def aumento(funcao):
    salary = funcao()
    new_salary = salary + ((salary*15)/100)
    return new_salary

final = aumento(entrada)
print(final)