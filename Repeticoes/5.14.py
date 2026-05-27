quantidade = 0
soma = 0

num = int(input("Digite um numero(0 para sair): "))
while num != 0:
    soma = soma + num
    quantidade = quantidade + 1

    num = int(input("Digite um numero(0 para sair): "))

if quantidade > 0:
    media = soma / quantidade
else :
    media = 0

print(f"Quantidade de numeros digitados: {quantidade}")
print(f"Soma dos numeros: {soma}")
print(f"Media dos numeros: {media}")