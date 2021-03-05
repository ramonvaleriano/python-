# Program: aula_09b.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 26/09/2020 - 22:00

frase = 'Curso em Vídeo Python'
print(frase[13:])
print(frase[1::2])

print('Oi')

print("""
CAUSALIDADE
Sexo causa gente.""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))

frase1 = '   Milla tem uma buceta Gigante    '
print(frase1)
print(frase1.strip())
print(frase1.replace('buceta', 'perna'))
print(frase1)
frase1 = frase1.replace('buceta', 'perna')
frase2 = 'Milla fode bem, sim!'
print(frase2)
frase2 = list(frase2)
print(frase2)
frase2 = "".join(frase2)
print(frase2)
frase2 = frase2.replace('sim', 'não')
print(frase2)
print('Sexo' in frase2)
print(frase.find('Curso'))
print(frase.find('curso'))
print(frase.lower().find('curso'))
print(frase.lower().find('video'))
print(frase2.split())
dividido = frase2.split()
print(dividido)
juntou = "-".join(dividido)
print(juntou)
print(dividido[2][3])