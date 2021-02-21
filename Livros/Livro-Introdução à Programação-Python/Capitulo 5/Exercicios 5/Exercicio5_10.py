# Program: Exercicio5_10.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 29/03/2020 - 17:53
# Update:

pontos = 0
questoes = 1

while questoes<=3:
    resposta = input("Resposta da questão %d." %questoes)
    resposta = resposta.lower()
    if questoes == 1 and resposta == "b":
        pontos+=1
    if questoes == 2 and resposta == "a":
        pontos+=1
    if questoes == 3 and respota == "d":
        pontos+=1
    questoes+=1
print(pontos)

