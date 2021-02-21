# Program: Exercicio7_1.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 19:07
# Updated:

word1 = str(input("Entre com uma nome qualquer: "))
word2 = str(input("Entre com um palavra qualquer: "))

if word2.upper() in word1.upper():
    test = word1.upper().find(word2.upper())
    print("A %s está dentro da frase 1, na posição: %d" %(word2, test))
else:
    print("A frase dois não está no frase 1.")
