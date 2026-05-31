n = int(input("Quantos números primos deseja imprimir? "))

quantidade = 0
numero = 2

while quantidade < n:
    primo = True

    if numero > 2 and numero % 2 == 0:
        primo = False
    else:
        divisor = 3
        while divisor * divisor <= numero:
            if numero % divisor == 0:
                primo = False
                break
            divisor += 2

    if primo:
        print(numero)
        quantidade += 1

    numero += 1