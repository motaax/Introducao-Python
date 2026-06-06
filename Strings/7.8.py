palavra = input("Digite a palavra secreta: ").lower().strip()

for _ in range(100):
    print()

digitadas = []
acertos = []
erros = 0

# Desenho inicial da forca
forca = [
    list("X==:=="),
    list("X  :  "),
    list("X     "),
    list("X     "),
    list("X     "),
    list("=======")
]

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "."

    print("\n" + senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue

    digitadas.append(tentativa)

    if tentativa in palavra:
        acertos.append(tentativa)
    else:
        erros += 1
        print("Você errou!")

        if erros == 1:
            forca[2][2] = "O"      # cabeça
        elif erros == 2:
            forca[3][2] = "|"      # tronco
        elif erros == 3:
            forca[3][1] = "\\"     # braço esquerdo
        elif erros == 4:
            forca[3][3] = "/"      # braço direito
        elif erros == 5:
            forca[4][1] = "/"      # perna esquerda
        elif erros == 6:
            forca[4][3] = "\\"     # perna direita

    # Exibe a forca
    for linha in forca:
        print("".join(linha))

    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break