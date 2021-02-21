# Program: Listagem8_10Global2.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 15:47
# Updated:

a = 5
def muda_e_imprime():
    global a
    a = 7
    print("A dentro da função {0}".format(a))
print("A antes da função {0}".format(a))
muda_e_imprime()
print("A depois da função {0}".format(a))
