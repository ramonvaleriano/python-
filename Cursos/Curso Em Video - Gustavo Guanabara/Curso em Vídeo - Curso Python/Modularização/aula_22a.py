# Program: aula_22a.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 08/10/2020 - 17:13

import uteis
from calculos_matematicos import fatorial, dobro, triplo

nummero = int(input('Digite um número: '))
fat = uteis.fatorial(nummero)
print(fat)
print(dobro(nummero))
print(triplo(nummero))



