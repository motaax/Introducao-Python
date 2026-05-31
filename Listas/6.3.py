lista1 = []
lista2 = []
lista3 = []

for i in range(3):
    valor = int(input(f"Digite o {i + 1}° numero da lista 1: "))
    lista1.append(valor)

for i in range(3):
    valor = int(input(f"Digite o {i + 1}° numero da lista 2: "))
    lista2.append(valor)

for num in lista1:
    if num not in lista3:
        lista3.append(num)

for num in lista2:
    if num not in lista3:
        lista3.append(num)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3 sem repeticao: {lista3}")