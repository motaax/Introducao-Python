deposito_inicial = float(input("Depósito inicial: R$ "))
deposito_mensal = float(input("Depósito mensal: R$ "))
taxa = float(input("Taxa de juros mensal (%): "))

saldo = deposito_inicial
mes = 1

while mes <= 24:
    saldo = saldo + deposito_mensal

    juros = saldo * (taxa / 100)
    saldo = saldo + juros

    print(f"Mês {mes}: R$ {saldo:.2f}")

    mes = mes + 1

total_depositado = deposito_inicial + (deposito_mensal * 24)
ganho = saldo - total_depositado

print(f"\nTotal depositado: R$ {total_depositado:.2f}")
print(f"Total ganho com juros: R$ {ganho:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")