# Program: Exercicio7_4.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 19:20
# Updated:

word = str(input("Entre com uma frase: "))
letters = list(word)

for e in letters:
    if e in word:
        test = word.count(e)
        print(e, test)
        

