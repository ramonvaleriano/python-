# Program: listagem9_3.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 11:51

import sys
print("Número de parâmetros: %d" %len(sys.argv))
for indice, elemento in enumerate(sys.argv):
    print(f'Parâmetros: {indice} = {elemento}')
