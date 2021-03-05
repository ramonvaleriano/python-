# Program: Algoritmo397_Vetor45.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 11/05/2020 - 19:33
# Updated:

clientes = list()
valores = list()
quantity = 10

while True:
    print("-"*15+"MENU"+"-"*15)
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar preço das costuras.")
    print("3 - Calcular e imprimir o total que")
    print("    sera pago por cada freguesa.")
    print("4 - Listar dados de uma cliente.")
    print("5 - Sair do Programa.")
    option = int(input("Qual opção deseja: "))
    if option == 5:
        print("Programa Finalizado!")
        break
    elif option == 1:
        dados = list()
        if cont<quantity:
            name = str(input("Entre com o nome da cliente: "))
            name = name.upper()
            dados.append(name)
            print("Digite as opção de Costura")
            print("que essa cliente irá fazer: ")
            print("Vestido")
            print("Calça")
            print("Saia")
            print("Blusa")
            print("Conjunto")
            print("Blase")
            tipo = str(input("--> "))
            tipo = tipo.upper()
            dados.append(tipo)
            if len(clientes)>0:
                cont1 = 0
                while cont1<len(clientes):
                    if clientes[cont][0] == name:
                        clientes[cont][1] = tipo
                    cont+=1
                else:
                    clientes.append(dados[:])
            else:
                clientes.append(dados[:])
        else:
            print("Não há mais opções para adicionar clientes!")
    elif option == 2:
        dados1 = list()
        print("Digite as opção de valores")
        print("da costura de forma individual: ")
        print("Vestido")
        print("Calça")
        print("Saia")
        print("Blusa")
        print("Conjunto")
        print("Blase")
        costura = str(input("--> "))
        costura = costura.upper()
        dados1.append(costura)
        value = float("Digite o valor dessa da %s: " %costura)
        dados1.append(value)
        if len(valores)>0:
            cont2 = 0
            while cont2<len(clientes):
                    if clientes[cont2][0] == costura:
                        clientes[cont2][1] = value
                    else:
                        valores.append(dados1[:])
                    cont2+=1
        else:
            valores.append(dados1[:])
    elif option == 3:
        if len(clientes)>0:
            sum_ = 0
            cont3 = 0
            while cont3<len(clientes):
                cont3_1 = 0
                while cont3_1<len(valores):
                    if clientes[cont3][0] == valores[cont3_1]:
                        pagar = valores[cont3_1]
                        sum_+=pagar
                        clientes[cont3].append(pagar)
                    cont3_1+=1
                cont3+=1
            for v in cliente:
                print("Cliente: %12s - Costura: %12s - Valor: R$%7.2f" %(v[0], v[1], v[2]))
            print("Lucro: R$%7.2f" %sum_)
        else:
            print("Não há clientes suficiente para isso!")
    elif option == 4:
        if len(clientes)>0:
            cont4 = 0
            while cont4<len(clientes):
                cont4_1 = 0
                while cont4_1<len(valores):
                    if clientes[cont4][0] == valores[cont4_1]:
                        pagar = valores[cont4_1]
                        sum_+=pagar
                        clientes[cont4].append(pagar)
                    cont4_1+=1
                cont4+=1
            procura = str(input("Qual cliente deseja procurar: "))
            procura = procura.upper()
            for e in clientes:
                if procura == e[0]:
                    print("%12s - %12s - R$%7.2f" %(e[0], e[1], e[2]))
                    break
            else:
                print("Não há esse cliente!")
            
