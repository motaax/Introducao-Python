ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("A para realizar atendimento e S para sair.")

    operacao = input("Operação: ").upper()

    for comando in operacao:
        if comando == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")

        elif comando == "F":
            ultimo += 1
            fila.append(ultimo)

        elif comando == "S":
            break

        else:
            print("Operação inválida:", comando)

    if "S" in operacao:
        break