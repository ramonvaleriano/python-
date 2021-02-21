# Program: Listagem6_18.py
# Author: Ramon R. Valeriano
# Description:  
# Developed: 19/04/2020 - 17:20
# Updated:

l = list()
print(l)
l+=["a"]
print(l)
l.append("b")
print(l)
l.extend(["c","d"])
print(l)
l.append(["e","f","g"])
print(l)
print("Há", len(l), "Elementos")
print(l[4][1])
print(l[4][0])
print(l[4][2])
print(len(l[4]))
