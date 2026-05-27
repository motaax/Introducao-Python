n = int(input("Tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

i = inicio

while i <= fim:
    print(f"{n} x {i} = {n * i}")
    i = i + 1