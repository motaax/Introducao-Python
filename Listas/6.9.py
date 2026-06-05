L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = int(input("Digite um numero a pesquisar: "))

for i in L:
    if  i == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento nao encontrado!")    