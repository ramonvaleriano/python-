# Program: desafio_069.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 18:23

q_maior = 0
q_homens = 0
q_m_menores = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa[M/F]: ')).upper().strip()[0]
    if idade>= 18:
        q_maior+=1
    if sexo == 'M':
        q_homens+=1
    elif sexo == 'F':
        if idade <=20:
            q_m_menores+=1
    else:
        print('Opção Invalida')
    opcao = str(input('Deseja Continuar[S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
    else:
        print('Preencha os novos dados: ')
print(q_maior)
print(q_homens)
print(q_m_menores)