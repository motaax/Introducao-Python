with open("pares.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("pares_invertido.txt", "w") as arquivo:
    for linha in reversed(linhas):
        arquivo.write(linha)