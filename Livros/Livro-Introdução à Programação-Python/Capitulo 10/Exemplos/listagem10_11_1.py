# Program: listagem10_11.py
# Author: Ramon R. Valeriano
# Decription:
# Developed: 27/02/2020 - 22:35

from contas2 import Conta

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self._limite = limite

    def saque(self, valor):
        if self.saldo + self._limite >= valor:
            self.saldo-=valor
            self._operacoes.append(["Saque", valor])
