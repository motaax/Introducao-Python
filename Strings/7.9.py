tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

posicoes = {
    7: (0, 0), 8: (0, 1), 9: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    1: (2, 0), 2: (2, 1), 3: (2, 2)
}


def mostrar_tabuleiro():
    print()
    print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("---+---+---")
    print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("---+---+---")
    print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")
    print()


def venceu(simbolo):
    # Linhas
    for linha in tabuleiro:
        if linha.count(simbolo) == 3:
            return True

    # Colunas
    for coluna in range(3):
        if (tabuleiro[0][coluna] == simbolo and
            tabuleiro[1][coluna] == simbolo and
            tabuleiro[2][coluna] == simbolo):
            return True

    # Diagonais
    if (tabuleiro[0][0] == simbolo and
        tabuleiro[1][1] == simbolo and
        tabuleiro[2][2] == simbolo):
        return True

    if (tabuleiro[0][2] == simbolo and
        tabuleiro[1][1] == simbolo and
        tabuleiro[2][0] == simbolo):
        return True

    return False


jogador = "X"
jogadas = 0

while True:
    mostrar_tabuleiro()

    try:
        posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if posicao not in posicoes:
        print("Posição inválida!")
        continue

    linha, coluna = posicoes[posicao]

    if tabuleiro[linha][coluna] != " ":
        print("Posição ocupada!")
        continue

    tabuleiro[linha][coluna] = jogador
    jogadas += 1

    if venceu(jogador):
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break

    if jogadas == 9:
        mostrar_tabuleiro()
        print("Empate!")
        break

    jogador = "O" if jogador == "X" else "X"