# Program: Algortimo395_Vetor43.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/05/2020 - 16:03
# Updated:

quantity = 15
cont = 0
agenda = list()
while cont<quantity:
    dados = list()
    print("-"*15+"MENU"+"-"*15)
    print("1 - Inserir")
    print("2 - Ordenar")
    print("3 - Listar")
    print("4 - Procurar")
    print("5 - Sair")
    number = int(input("Entre com a opção desejada: "))
    print("\n\n")
    if number == 5:
        break
    elif number == 1:
        name = str(input("Entre com um nome: "))
        name = name.upper()
        salary = float(input("Enter com um salario: "))
        dados.append(name)
        dados.append(salary)
        agenda.append(dados[:])
    elif number == 2:
        if len(agenda)>1:
            cont1 = 0
            while cont1<len(agenda):
                cont2 = 0
                while cont2<len(agenda):
                    if agenda[cont1][0]>agenda[cont2][0]:
                        agenda[cont1], agenda[cont2] = agenda[cont2], agenda[cont1]
                    cont2+=1
                cont1+=1
            for e in agenda:
                print("%+12s - R$%7.2f" %(e[0], e[1]))
        else:
            print("Invalido!")
    elif number == 3:
        if len(agenda)>0:
            for e in agenda:
                print("%+12s - R$%7.2f" %(e[0], e[1]))
        else:
            print("Invalido!")
    elif number == 4:
        if len(agenda)>0:
            procura = str(input("Qual nome deseja procurar: "))
            procura = procura.upper()
            achou = False
            for n in agenda:
                if procura == n[0]:
                    sal = n[1]
                    achou = True
            if acho:
                print("Nome encontrado: ", procura)
                print("Salario: R$%7.2f" %sal)
            else:
                print("Nome não encontrado")
        else:
            print("Invalido!")
    else:
        print("Opção Invalida!")
                
            
