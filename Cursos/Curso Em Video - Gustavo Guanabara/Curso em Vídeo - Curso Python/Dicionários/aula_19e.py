# Program: aula_19e.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 06/10/2020 - 17:12

pessoa = {'nome': 'Ramon R. Valeriano', 'sexo': 'Masculino', 'idade': 31}
print(pessoa['nome'])
print(pessoa['sexo'])
print(f'O {pessoa["nome"]} é do sexo {pessoa["sexo"]} com {pessoa["idade"]} anos')
print(pessoa.keys())
print(pessoa.values())
for k in pessoa.keys():
    print(k.title())
print()
for v in pessoa.values():
    print(str(v).title())
print()
for chave, valor in pessoa.items():
    print(f'{chave.title()} >> {str(valor).title()}')
print()
del pessoa['sexo']
for chave, valor in pessoa.items():
    print(f'{chave.title()} >> {str(valor).title()}')
print()
pessoa['nome'] = 'Vagner'
for chave, valor in pessoa.items():
    print(f'{chave.title()} >> {str(valor).title()}')
print()
pessoa['nome'] = 'Ramon'
pessoa['peso'] = 98.5
for chave, valor in pessoa.items():
    print(f'{chave.title()} >> {str(valor).title()}')