# Program: Algoritmo12_se3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 10:53
# Updated:

verb = input("Enter with the verb: ")
number = len(verb)
last = verb[number-1]
#print(last)
#print("This is programa works so las!")
if(last == "R")or(last == "r"):
    print("Esse Verbo está no infinitivo!")
    indicator = verb[number-2]
    if(indicator == "a")or(indicator == "A"):
        print("1° COnjugação!")
    elif(indicator == "e")or(indicator == "E")or(indicator == "o")or(indicator == "O"):
        print("2° Conjugação!")
    elif(indicator == "i")or(indicator == "I"):
        print("3° Conjugação!")
    else:
        print("You are asshole!")
else:
    print("What fuck is this?!")
