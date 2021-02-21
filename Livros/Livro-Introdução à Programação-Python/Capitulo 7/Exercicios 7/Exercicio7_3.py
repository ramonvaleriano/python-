# Program: Exercicio7_3.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 19:10
# Updated:

word = str(input("Enter com uma frase: "))
name = str(input("Enter com um nome: "))
letters = list(name)
quanitity = len(letters)
new_word = list()
for e in letters:
    if e not in word:
        new_word.append(e)
new_word="".join(new_word)
print()
print(new_word)
