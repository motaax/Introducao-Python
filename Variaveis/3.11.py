preco = float(input("Digite o preco: R$ "))
desconto = int(input("Digite o desconto: % "))

novo_desconto = preco * (desconto / 100)
novo_preco = preco - novo_desconto

print(f"O valor do desconto: R$ {novo_desconto:.2f}")
print(f"Novo preco: R$ {novo_preco:.2f}")