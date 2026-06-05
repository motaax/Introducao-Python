ultimo = 0
fila1 = []
fila2 = []

while True:
    print("\nFila 1:", fila1)
    print("Fila 2:", fila2)

    print("\nF - Novo cliente na fila 1")
    print("G - Novo cliente na fila 2")
    print("A - Atender cliente da fila 1")
    print("B - Atender cliente da fila 2")
    print("S - Sair")

    operacao = input("Operação: ").upper()

    for comando in operacao:

        if comando == "F":
            ultimo += 1
            fila1.append(ultimo)
            print(f"Cliente {ultimo} entrou na fila 1")

        elif comando == "G":
            ultimo += 1
            fila2.append(ultimo)
            print(f"Cliente {ultimo} entrou na fila 2")

        elif comando == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido na fila 1")
            else:
                print("Fila 1 vazia!")

        elif comando == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido na fila 2")
            else:
                print("Fila 2 vazia!")

        elif comando == "S":
            break

        else:
            print(f"Operação inválida: {comando}")

    if "S" in operacao:
        break