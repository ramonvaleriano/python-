# Program: Algoritmo155_se66.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 14:01
# Updated:

word = input("Enter wiht a word: ")
word = word.upper()
first = word[0]
if(first == "L")or(first == "D"):
    new_word = word[0:2]+word[-1]
    print(new_word)
else:
    new_word = word[1:]
    print(new_word)


