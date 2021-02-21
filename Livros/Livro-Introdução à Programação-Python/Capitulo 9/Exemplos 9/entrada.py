# Program: entrada.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 13:26

entrada = open("entrada.txt", "w")

entrada.write(f';Esta linha não deve ser impressa.\n')
entrada.write(f'>Esta linha deve ser impressa alinha da a direita.\n')
entrada.write(f'*Esta linha deve ser centralizada.\n')
entrada.write(f'Uma linha normal\n')
entrada.write(f'Outra linha normal.\n')
entrada.close()
