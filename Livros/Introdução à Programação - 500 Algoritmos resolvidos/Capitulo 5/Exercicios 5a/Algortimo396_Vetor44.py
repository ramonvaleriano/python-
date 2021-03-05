# Program: Algortimo396_Vetor44.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/05/2020 - 17:33
# Updated:


programacao = list()
sistemas = list()
quantity = 100
contp = 0
conts = 0
while True:
    name = str(input("Digite o nome do aluno: "))
    matricula = int(input("Digte a matricula do aluno: "))
    dados.append(name)
    dados.append(matricula)
    print("Digite para qual matéria deseja que o aluno seja inscrito. ")
    print("1 - Programaçao I")
    print("2 - Sistemas de Informação")
    print("3 - Nas duas matérias.")
    print("4 - Sair.")
    opcao = int(input("Digite a opÇão desejada: "))
    if opcao == 4 or (contp==100 and conts==100):
        break
    elif opcao == 1:
        if contp<=quantity:
            programacao.append(dados[:])
            contp+=1
        else:
            print("Sala Lotada!")
    elif opcao == 2:
        if conts<=quantity:
            sistemas.append(dados[:])
            conts+=1
        else:
            print("Sala Lotada!")
    elif opcao == 3:
        if contp<=quantity and conts<=quantity:
            programacao.append(dados[:])
            sistemas.append(dados[:])
            contp+=1
            conts+=1
        else:
            print("Salas Lotadas!")
    else:
        print("Opção Invalida!")
while True:
    print("Digite quais turmas deseja mostrar:")
    print("1 - Programaçao I")
    print("2 - Sistemas de Informação")
    print("3 - Procurar")
    print("4 - Sair.")
    opcao = int(input("Digite a opÇão desejada: "))
    if opcao == 4:
        break
    elif opcao == 1:
        for e in programacao:
            print(e[0],e[1])
    elif opcao == 2:
        for e in sistemas:
            print(e[0],e[1])
    elif opcao == 3:
        mat = str(input("Enter com a matricula que deseja procurar: "))
        achou1 = False
        achou2 = False
        for p in programcao:
            if p[1] == mat:
                achou1 = True
        for s in sistemas:
            if s[1] == mat:
                achou2 = True
        if achou1:
            print("Está Matriculado na Turma de Programação!")
        if achou2:
            print("Está Matriculado na Turma de Programação!")
        if achou1 and achou2:
            print("Está matriculado nas duas turmas!")
    else:
        print("Opção Invalida!")
