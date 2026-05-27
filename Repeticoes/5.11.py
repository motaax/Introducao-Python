deposito = float(input("Deposito inicial: R$ "))
taxa = float(input("Taxa de juros mensal (%): "))

saldo = deposito
mes = 1

while mes <= 24:
    juros = saldo * (taxa / 100)
    saldo = saldo + juros

    print(f"Mês {mes}: R$ {saldo:.2f}")

    mes = mes + 1

ganho = saldo - deposito

print(f"\nTotal ganho com juros: R$ {ganho:.2f}")