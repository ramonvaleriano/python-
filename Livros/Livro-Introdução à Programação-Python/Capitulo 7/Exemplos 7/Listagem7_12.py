# Program: Listagem7_12.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 18:59
# Updated:

s = "Um tigre, dois tigres, três tigres"
p = 0
while (p>-1):
    p=s.find("tigre", p)
    if p>=0:
        print("Posição: %d" %p)
        p+=1
    
