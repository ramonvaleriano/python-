# Program: Algoritmo266_Enq5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:18
# Updated:

cont = 0
word = input("Enter with a %d° word: " %(cont+1))
word = word.upper()
test = word[0]

while word!="FIM":
    cont+=1
    print("\n%s\n" %test)
    word = input("Enter with a %d° word: " %(cont+1))
    word = word.upper()
    test = word[0]
    
