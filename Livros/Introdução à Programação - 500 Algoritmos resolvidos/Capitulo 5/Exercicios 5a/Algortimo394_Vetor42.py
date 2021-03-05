# Program: Algortimo394_Vetor42.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/05/2020 - 12:35
# Updated: 09/05/2020 - 15:05

quantity = 50
cont = 0
classe = dict()
tax1 = 3
tax2 = 7
while True:
    print("-"*15+"MENU"+"-"*15)
    print("1 - Entrar com nome.")
    print("2 - Entrar com a primeira nota.")
    print("3 - Entrar com a segunda nota.")
    print("4 - Calcular a media.")
    print("5 - Lista no display.")
    print("6 - Sair.")
    number = int(input("Entre com a opção desejada: "))
    print("\n\n")
    dados = [-1,-1,-1]
    if number == 6:
        break
    elif number == 1:
        print("\n")
        if cont<quantity:
            name = str(input("Entre com o nome do aluno: "))
            classe[name]=dados[:]
            cont+=1
        else:
            print("Não há mais espaço para alunos!")
     elif number == 2:
         print("\n")
         if len(classe)>0:
             name_test = str("Para qual aluno deseja adicionar a Primeira nota: ")
             if (name_test in classe):
                 note = float(input("Enter com a primeira nota: "))
                 if note>=0 and note<=10:
                     classe[name_test][0]=note
                 else:
                     print("Nota Invalida!")
            else:
                print("Não há esse aluno na turma!")
        else:
            print("Não há aluno para por nota!")
     elif number == 3:
         print("\n")
         if len(classe)>0:
             name_test = str("Para qual aluno deseja adicionar a Segunda nota: ")
             if (name_test in classe):
                 note = float(input("Enter com a Segunda nota: "))
                 if note>=0 and note<=10:
                     classe[name_test][1]=note
                 else:
                     print("Nota Invalida!")
            else:
                print("Não há esse aluno na turma!")
        else:
            print("Não há aluno para por nota!")
    elif number == 4:
        print("\n")
        if len(classe)>0:
             name_test = str("Para qual aluno deseja adicionar a Primeira nota: ")
             if (name_test in classe):
                 if classe[name_test][0]>=0 and classe[name_test][1]>=0:
                     media = ((tax1*(classe[name_test][0]))+(tax2*(classe[name_test][1])))/(tax1+tax2)
                     classe[name_test][2]=media
                 else:
                     print("Não há como Calcular a media!")
             else:
                 print("Não há aluno com esse nome: ")
        else:
            print("Não há Alunos suficientes!")
    elif number == 5:
        print("\n")
        if len(classe)>0:
            for k, v in classe.items():
                if v[0]<0:
                    v[0]=0
                if v[1]<0:
                    v[1]=0
                if v[2]<0:
                    v[2]=0
                print("%+12s - %4.2f - %4.2f = %4.2f" %(k, v[0],v[1],v[2]))
        else:
            print("Não há Alunos suficientes!")
    else:
        print("Opção Invalida!")
    print("\n")
        
