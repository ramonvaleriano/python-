# Program: Exemplos_VideoAula10.py 
# Author: Ramon R. Valeriano
# Description: Exemplos de Video aula, DICIONÁRIO
# Developed: 27/04/2020 - 23:29
# Updated:

aluno = dict()
name = str(input("Enter with the name: "))
aluno["Nome"]=name
media = float(input("Enter with the media: "))
aluno["Media"]=media
if media >= 0 and media < 7:
    status = "Reprovado"
elif media >= 7 and media <=10:
    status = "Aprovado"
else:
    status = "Não existe"
aluno["Status"]=status
print(aluno)
    
