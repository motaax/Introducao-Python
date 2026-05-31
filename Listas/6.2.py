lista1 = []
lista2 = []

for i in range(3):
    valor = int(input(f"Digite o {i + 1}° da lista 1: "))
    lista1.append(valor)

for i in range(3):
    valor = int(input(f"Digite o {i + 1}° da lista 2: "))
    lista2.append(valor)

lista3 = lista1 + lista2
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")