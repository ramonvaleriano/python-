# Program: Algoritmo399_Vetor47.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 11/05/2020 - 22:07
# Updated:

agenda = dict()

while True:
    print("-"*20+"Lista Telefonica"+"-"*20)
    print("1 - Inclusão de Novo Número.")
    print("2 - Alterar Telefone")
    print("3 - Apagar Telefone")
    print("4 - Impressão de Todos os telefones")
    print("5 - Consultar por nome ")
    print("6 - Sair")
    option = int(input("Entrea com a opção desejada: "))
    print("-"*20+"-"*16+"-"*20)
    print("\n\n")
    if option == 6:
        break
    elif option == 1:
        name = str(input("Digite o nome da pessoa que deseja adicionar: "))
        numero = int(input("Digite o número do telefone: "))
        agenda[name]=numero
    elif option == 2:
        if len(agenda)>0:
            name = str(input("Digite o nome da pessoa que deseja mudar o número: "))
            if (name in agenda):
                numemro = int(input("Para qual número deseja mudar: "))
                agenda[name]=numero
            else:
                print("Não há nome registrado!")
        else:
            print("Não há pessoas Registrada!")
    elif option == 3:
        if len(agenda)>0:
            name = str(input("Digite registro que deseja apagar: "))
            if (name in agenda):
                del agenda[name]
            else:
                print("Não há ese registro!")
        else:
            print("Não há pessoas registradas para essa opção!")
    elif option == 4:
        if len(agenda)>0:
            for k, v in agenda.items():
                print("%+12s - %d" %(k, v))
        else:
            print("Não há registros!")
    elif option == 5:
        if len(agenda)>0:
            name = str(input("Digite o nome que deseja procurar: "))
            if (name in agenda):
                test = agenda[name]
                print("%+12s - %d" %(name, test))
            else:
                print("Não Há resgistro!")
        else:
            print("Não Há resgistro!")
    else:
        print("Opção Invalida!")
    print("\n\n")
