# Program: Exercicio7_5.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 19:20
# Updated:

word1 = str(input("Entre com o primeito nome: "))
word2 = str(input("Entre com o segundo nome:"))
lettres = list(word1)
word3 = list()
for e in lettres:
    if e not in word2:
        word3.append(e)

word3="".join(word3)
print(word3)
        
