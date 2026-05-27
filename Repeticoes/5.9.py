dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

quociente = 0
resto = dividendo

while resto >= divisor:
    resto = resto - divisor
    quociente = quociente + 1

print("Quociente:", quociente)
print("Resto:", resto)