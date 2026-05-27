kwh = float(input("Quantidade de kWh consumida: "))
tipo = input("Tipo de instalação (R, C ou I): ").upper()

if tipo == "R":
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65

elif tipo == "C":
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60

elif tipo == "I":
    if kwh <= 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60

else:
    preco = 0
    print("Tipo de instalação inválido!")

if preco > 0:
    print(f"Valor a pagar: R$ {preco:.2f}")