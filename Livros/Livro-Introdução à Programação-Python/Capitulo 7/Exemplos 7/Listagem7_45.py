# Program: Listagem7_45.py
# Author: Ramon R. Valeriano
# Description: Jogo da forca
# Developed: 19/05/2020 - 19:45
# Updated: 19/05/2020 - 20:23

palavra = input("Digite a palavra secreta: ").lower().strip()

for x in range(100):
    print()

digitados = []
acertos = []
erros = 0

while True:
    senha=""
    for letra in palavra:
        senha+=letra if letra in acertos else "."
        print(senha)
    if senha == palavra:
        print("Você acertou")
        break
    tentativa = input("Digite um letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você Errou!")
    print("X==:==\nX : ")
    print("X 0 " if erros>= 1 else "X")
    linha2=""
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " \| "
    elif erros >= 4:
        linha2 = "\|/"
    print("X%s" % linha2)
    linha3=""
    if erros == 5:
        linha3+=" / "
    elif erros>=6:
        linha3+=" / \ "
        print("x%s" % linha3)
        print("X\n=========")
    if erros == 6:
        print("Enforcado")
        break
        
