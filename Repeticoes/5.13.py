divida = float(input("Valor inicial da dívida: R$ "))
juros = float(input("Juro mensal (%): "))
pagamento = float(input("Valor pago por mês: R$ "))

meses = 0
total_pago = 0
total_juros = 0

while divida > 0:
    valor_juros = divida * (juros / 100)
    divida = divida + valor_juros

    total_juros = total_juros + valor_juros

    if pagamento > divida:
        pagamento_mes = divida
    else:
        pagamento_mes = pagamento

    divida = divida - pagamento_mes

    total_pago = total_pago + pagamento_mes
    meses = meses + 1

    print(f"Mês {meses}: dívida restante = R$ {divida:.2f}")

print("\nDívida quitada!")
print(f"Quantidade de meses: {meses}")
print(f"Total pago: R$ {total_pago:.2f}")
print(f"Total de juros pagos: R$ {total_juros:.2f}")