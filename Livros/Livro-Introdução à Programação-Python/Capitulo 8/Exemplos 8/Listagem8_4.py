# Program: Listagem8_4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/06/2020 - 20:27
# Updated:

def ehpar(x):
    return(x%2==0)
def par_ou_impa(x):
    if ehpar(x):
        return "É Par!"
    else:
        return "É Impá!"

print(par_ou_impa(4))
print(par_ou_impa(5))
