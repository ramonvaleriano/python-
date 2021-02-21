# Program: Listagem7_11.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 18:47
# Updated:

s = "Um tigre, dois tigres, três tigres"
test = s.find("tigre")
print(test)
test = s.find("tigres")
print(test)
test = s.rfind("tigres")
print(test)
test = s.find("tigres", 7)
print(test)
test = s.find("tigres", 30)
print(test)
test = s.find("tigres", 0, 10) #Incio = 0 ; Fim = 10
print(test)
