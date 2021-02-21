# Program: Exercicio7_6.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 16/05/2020 - 19:51
# Updated:

s1 = str(input("Entre com o primeiro nome: "))
s2 = str(input("Entre com o segundo nome: "))
s3 = str(input("Entre com o terceiro nome: "))
quantity = list()
wt = list(s2)
wn = list(s3)


for n in s2:
    if n in s1:
        number = s1.find(n)
        quantity.append(number)
wf = list(s1)
new = list()
cont = 0
for e in wf:
    if e not in s2:
        new.append(e)
    elif e in s2:
        new.append(wn[0])
        cont+=1
new="".join(new)
print(new)
