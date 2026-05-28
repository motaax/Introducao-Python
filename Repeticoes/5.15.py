total = 0

while True:
    codigo = int(input("Digite o codigo do produto(0 para sair): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade comprada: "))

    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Codigo invalido!")
        continue

    total += preco * quantidade

print(f"Total das compras: R$ {total:.2f}")