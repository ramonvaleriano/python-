# Program: Algortimo390_Vetor38Tentando.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/05/2020 - 09:15
# Updated:

agenda = dict()
quantity = 5
for e in range(quantity):
    name = str(input("Enter with %d° name: " %(e+1)))
    name = name.upper()
    dados = list()
    cpf = int(input("Enter with the %d° CPF: " %(e+1)))
    dados.append(cpf)
    profission = str(input("Enter with the %d° profission: " %(e+1)))
    profission = profission.upper()
    dados.append(profission)
    agenda[name] = dados[:]
print("\n")
test = list()
last = 0 
for n in agenda.values():
    test.append(n[-1])
profissoes = list()
cont = 0
while cont<len(test):
    dados = list()
    cont2 = 0
    point = 0
    prof = test[cont]
    while cont2<len(test):
        if test[cont]==test[cont2]:
            point+=1
        cont2+=1
    if point>1:
        dados.append(test[cont])
        dados.append(point)
        profissoes.append(dados)
    cont+=1
cont = 0
while cont<len(profissoes):
    cont2 = 0
    while cont2<len(profissoes):
        if profissoes[cont][0] == profissoes[cont2][0]:
            del profissoes[cont2]
        cont2+=1
    cont+=1
for n in profissoes:
    print("%+12s - %d" %(n[0], n[1]))
    
            
        
        
