# Program: listagem10_11.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 22:42

from contas2 import Conta
from clientes import Cliente
from listagem10_9 import Banco
from listagem10_11 import ContaEspecial


joao = Cliente("João da Silva", '79846')
ramon = Cliente('Ramon Valeriano', '123456789')
maria = Cliente("Maria Jose", '321654')
milla = Cliente("Milla Gabriela", "45678913257")

contaj = Conta([joao, maria], 100)
contar = Conta([ramon], 10)
contg = ContaEspecial([milla], 2, 50000, 5000)

tatu = Banco('Tatu')

contg.saque(500)


