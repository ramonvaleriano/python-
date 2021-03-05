# Program: Algoritmo143_se54.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 08:23
# Updated:

word = input("Enter with a word: ")

number = len(word)
print(number)
number = int(number)
word = word.upper()

if number%2!=0:
    test = int((number-1)/2)
    letter = word[test]
    print(letter)
    if(letter == "A")or(letter == "E")or(letter == "I")or(letter == "O")or(letter == "U"):
        print("É uma vogal!")
    else:
        print("Não é uma vogal!")
else:
    test = int((number-1)/2)
    letter = word[test]
    print(letter)
    previous = test-1
    letter_p = word[previous]
    posterior = test+1
    letter_po = word[posterior]
    if(letter == "R")or(letter == "S"):
        if(letter == "R")and((letter_p == "R")or(letter_po == "R")):
            print("RR")
        elif(letter == "S")and((letter_p == "S")or(letter_po == "S")):
            print("SS")
    else:
        print("Não deu em nada!")
        
    
    
    
