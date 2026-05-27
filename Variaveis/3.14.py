km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias alugados: "))

preco_dias = dias * 60
preco_km = km * 0.15

total = preco_dias + preco_km

print(f"Preço a pagar: R$ {total:.2f}")