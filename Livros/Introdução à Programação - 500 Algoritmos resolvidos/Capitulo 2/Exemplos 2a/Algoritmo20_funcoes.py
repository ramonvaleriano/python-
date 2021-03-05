# Program: Algoritmo20_funcoes.py
# Author: Ramon R. Valeraino
# Description:
# Developed: 13/03/2020 - 15:11
# Updated:

word1 = input("Enter with the first word: ")
word2 = input("Enter with the second word: ")

number_word = len(word1)
word1+=word2

word3 = word1[:]

print(number_word)
print(word1)
print(word3)

word4 = word1+word2
print(word4)
print(word1[0])
print(word1[-1])
print(word1[1:])
print(word1[:3])
print(word1[-3:])

