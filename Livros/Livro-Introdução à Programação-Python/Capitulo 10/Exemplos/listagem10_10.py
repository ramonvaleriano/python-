# Program: listagem10_10.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 21:51

from contas2 import Conta
from clientes import Cliente
from banco import Banco


joao = Cliente("João da Silva", '79846')
ramon = Cliente('Ramon Valeriano', '123456789')
maria = Cliente("Maria Jose", '321654')

contaj = Conta([joao, maria], 100)
contar = Conta([ramon], 10)
tatu = Banco('Tatu')

tatu.abre_conta(contaj)
tatu.abre_conta(contar)
tatu.lista_contas()