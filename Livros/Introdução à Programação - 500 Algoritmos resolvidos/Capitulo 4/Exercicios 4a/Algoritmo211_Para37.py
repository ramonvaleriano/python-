# Program: Algoritmo211_Para37.py
# Author: Ramon R. Valeriano
# Descripton:
# Developed: 02/04/2020 - 17:36
# Updated:

maximum = 100
for e in range(10, maximum+1):
    int(e)
    test1 = int(e%10)
    test2 = int(e/10)
    if test1!=0 and e%test2==0:
        print(e)
        
