salario = float(input("Digite o seu salario: R$ "))
porcentagem = int(input("Digite a porcentagem do aumento: "))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print(f"O valor do aumento: R$ {aumento:.2f}")
print(f"Novo salario: R$ {novo_salario:.2f}")