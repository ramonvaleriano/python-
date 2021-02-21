# Program: Listagem8_4DeNovo.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 11:19
# Updated:

def ehpar(x):
    return(x%2==0)
def par_ou_impar(x):
    if ehpar(x):
        return "É par!"
    else:
        return "É Impar!"
print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(10))
