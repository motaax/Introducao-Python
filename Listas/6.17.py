estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

total = 0

while True:
    produto = input("Produto (ou 'fim' para encerrar): ").lower()

    if produto == "fim":
        break

    if produto not in estoque:
        print("Produto não encontrado!\n")
        continue

    quantidade = int(input("Quantidade vendida: "))

    if quantidade > estoque[produto][0]:
        print("Estoque insuficiente!\n")
        continue

    preco = estoque[produto][1]
    custo = preco * quantidade

    estoque[produto][0] -= quantidade
    total += custo

    print(f"Venda registrada: {produto} - {quantidade} unidades")
    print(f"Valor da venda: R$ {custo:.2f}\n")

print(f"\nCusto total das vendas: R$ {total:.2f}\n")

print("Estoque atualizado:\n")

for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print("Preço: R$ %.2f\n" % dados[1])