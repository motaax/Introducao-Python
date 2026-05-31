while True:
    valor = int(input("Digite o valor a pagar (0 para sair): "))

    if valor == 0:
        break

    apagar = valor
    atual = 50

    while True:
        cedulas = 0

        while atual <= apagar:
            apagar -= atual
            cedulas += 1

        print(f"{cedulas} cédula(s) de R${atual}")

        if apagar == 0:
            break

        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1