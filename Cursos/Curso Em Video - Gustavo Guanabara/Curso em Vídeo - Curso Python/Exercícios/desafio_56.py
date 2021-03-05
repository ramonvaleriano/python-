# Program: desafio_056.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 28/09/2020 - 21:26

soma_idade = 0
geral = list()
quantidade = 3
for i in range(quantidade):
    dados = list()
    name = str(input('Digite o nome da %d° pessoa: ' %(i+1)))
    age = int(input('Digite a idade da %d° pessoa: ' %(i+1)))
    sex = str(input('Digite o sexo da %d° pessoa: ' %(i+1)))
    sex = sex.upper()
    soma_idade+=age
    dados.append(name)
    dados.append(age)
    dados.append(sex)
    geral.append(dados[:])

maior = geral[0][1]
name_maior = 0
cont_f = 0
media = soma_idade/quantidade

for x, i in enumerate(geral):
    if i[1]>=maior:
        maior = i[1]
        name_maior = i[0]
    elif i[2] == 'FEMININO' and i[1]<20:
        cont_f+=1
print(media)
print(name_maior)
print(cont_f)