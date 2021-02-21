# Program: Listagem6_22.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 13:35
# Updated:

pratos = 5
pilha = list(range(1, pratos+1))

while True:
    print("\nExistem %d pratos na pilha." %len(pilha))
    print("Pilha atual", pilha)
    print("Digete E para Empilhar um novo prato,")
    print("ou D para Desempilhar. S para Sair!")
    operacao = input("Entre com uma opção: E, D ou S")
    operacao = operacao.upper()
    if operacao == "D":
        if len(pilha)>0:
            lavado = pilha.pop(-1)
            print("Prato %d lavado:" %lavado)
        else:
            print("Pilha de pratos lavados. Nada para Lavar!")
    elif operacao == "E":
        pratos+=1
        pilha.append(pratos)
    elif operacao == "S":
        break
    else:
        print("Não há essa opção.")
print("\n\n",pilha,"\n\n")
