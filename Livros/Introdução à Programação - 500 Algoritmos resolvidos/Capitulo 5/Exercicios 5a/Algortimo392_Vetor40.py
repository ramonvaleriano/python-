# Program: Algortimo392_Vetor40.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/05/2020 - 10:58
# Updated:

quantity = 4
sum_ = 0
classe = list()

for e in range(quantity):
    dados = list()
    note = float(input("Entre com a nota do %d° Candidato: " %(e+1)))
    dados.append(note)
    sum_+=note
    name = str(input("Nome do %d° candidate: " %(e+1)))
    name = name.upper()
    dados.append(name)
    classe.append(dados)
media =  sum_/quantity
cont = 0
print()
print(media)
print()
while cont<len(classe):
    cont2 = 0
    while cont2<len(classe):
        if classe[cont][0]>classe[cont2][0]:
            classe[cont], classe[cont2] = classe[cont2], classe[cont]
        cont2+=1
    cont+=1
for n in classe:
    print("%5.2f - %-12s" %(n[0], n[1]))
print("\n\n")
while True:
    testando = True
    print("Pesquisa de Candidato -- > FIM, sai da busca!")
    test = str(input("Nome do Candidato que deseja procurar: "))
    if test.upper() == "FIM":
        break
    cont = 0
    while cont<len(classe):
        #testando = test.upper()
        if classe[cont][1] == test.upper():
            print("\nCandidato Encontrado: %-12s" %(test))
            print("Ele está na %d° colocação." %(cont+1))
            testando = False
            cont+=1
    if testando:
        print("Candidato não encontrado!")
