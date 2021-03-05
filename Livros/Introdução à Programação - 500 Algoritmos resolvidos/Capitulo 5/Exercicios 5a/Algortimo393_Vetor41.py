# Program: Algortimo393_Vetor41.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/05/2020 - 11:46
# Updated:

armazem = dict()
quantity = 40

for e in range(quantity):
    sum_=0
    print("\n")
    print("-"*15+"MENU"+"-"*15)
    print("1 - Cadastrar Mercadoria. ")
    print("2 - Exibir valor total em mercadoria da empresa.")
    print("3 - Sair do Programa.")
    number = int(input("Enter com sua opção: "))
    if number == 3:
        break
    elif number == 1:
        dados = list()
        name = str(input("Enter com o nome da mercadoria: "))
        name = name.upper()
        quantidade = int(input("Entre com a quantidade em estoque: "))
        dados.append(quantidade)
        individual = float(input("Entre com o valor unitário: "))
        dados.append(individual)
        armazem[name]=dados[:]
    elif number == 2:
        if len(armazem) > 0:
            for k, v in armazem.items():
                value = v[0]*v[1]
                sum_+=value
                print("%+12s -> %05d -> R$%7.2f = R$%7.2f" %(k, v[0], v[1], value))
            print("Total == R$%10.2f" %(sum_))
            print("\n")
        else:
            print("\n")
            print("Não há uma quantidade Suficiente para isso!")
            print("\n\n")
    else:
        print("Opção Invalida!")
            
            
