# Program: aula_17a.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 02/10/2020 - 14:13

#num = 2, 3, 9, 1
num = [2, 3, 8, 1]
print(num)
num[2]=3
num+=[7]
num.append(23)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
quantidade = len(num)
print(f'Nessa lista há {quantidade} elementos')
num.insert(2, 0)
print(num)
removeu = num.pop(0)
print(f'Removemos o elemento {removeu}')
print(num)
num.remove(2)
print(num)
if 3 in num:
    num.remove(3)
else:
    print('Não Achei')
print(num)