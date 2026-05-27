n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

resultado = 0
i = 0

while i < n2:
    resultado = resultado + n1
    i = i + 1

print("Resultado da multiplicação:", resultado)