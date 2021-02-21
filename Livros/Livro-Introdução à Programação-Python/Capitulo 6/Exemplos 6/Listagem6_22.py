# Program: Listagem6_22.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 20:48
# Updated:

pratos = 5
pilha = list(range(1, pratos+1))

while True:
    print("\nExistem %d pratos no pilha." %(len(pilha)))
    print("Pilha atual: ", pilha)
    print("Digite E para Empilhar um novo prato,")
    print("ou D para Desempilhar. S para Sair.")
    operacao = input("Operação(E, D ou S): ")
    operacao = operacao.upper()
    if operacao == "D":
        if len(pilha)>0:
            lavado = pilha.pop(-1)
            print("O prato %d foi lavado." %lavado)
        else:
            print("Não há mais pratos para se lavar!")
    elif operacao == "E":
        pratos+=1 #Adicionarmos mais um prato no pilha.
        pilha.append(pratos)
    elif operacao == "S":
        break
    else:
        print("Opção Invalida!")
