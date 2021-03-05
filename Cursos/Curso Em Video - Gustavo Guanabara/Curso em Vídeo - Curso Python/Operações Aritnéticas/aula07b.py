# Programa: aula_7b.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 21:43

def soma(num1, num2):
    return (num1 + num2)
def subrtracao(num1, num2):
    return (num1 - num2)
def multiplicacao(num1, num2):
    return (num1 * num2)
def divisao(num1, num2):
    return (num1 /  num2)
def div_inteiro(num1, num2):
    return (num1 // num2)
def resto(num1, num2):
    return (num1 % num2)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(soma(n1, n2), end=' ')
print(subrtracao(n1, n2), end=' ')
print(multiplicacao(n1, n2))
print(divisao(n1, n2))
print(div_inteiro(n1, n2))
print(resto(n1, n2))