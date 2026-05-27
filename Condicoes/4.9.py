valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário do comprador: R$ "))
anos = int(input("Digite a quantidade de anos para pagar: "))

meses = anos * 12

prestacao = valor_casa / meses

limite = salario * 0.30

print(f"\nValor da prestação mensal: R$ {prestacao:.2f}")

if prestacao <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")