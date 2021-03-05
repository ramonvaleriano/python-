# Program: Algoritmo385_Vetor33.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/05/2020 - 19:55
# Updated:

gabarito = list()
questions = 3
team = dict()
students = 2

for e in range(questions):
    letter = str(input("Entre com o gabarito de %d° questão: "%(e+1)))
    letter = letter[0].upper()
    gabarito.append(letter)
for n in range(students):
    stud = list()
    name = str(input("Entre com o nome do aluno: "))
    register = int(input("Entre com a matricula do aluno: "))
    stud.append(register)
    for g in range(questions):
        letter = str(input("Entre com o gabarito de %d° questão: "%(g+1)))
        letter = letter[0].upper()
        stud.append(letter)
    team[name]=stud[:]
for k, v in team.items():
    print(k)
    cont = 1
    point = 0
    for i, e in enumerate(v):
        if i == cont:
            if e==gabarito[cont-1]:
                point+=1
        cont+=1
    team[k].append(point)
for k, v in team.items():
    print("%12s - %d" %(k, v[-1]))
        
