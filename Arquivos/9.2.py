arquivo = open("arquivo.txt", "r")

for linha in arquivo.readlines():
    print(linha)
arquivo.close()