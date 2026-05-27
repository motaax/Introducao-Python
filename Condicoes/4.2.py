vel = float(input("Digite a velocidade do carro(km/h): "))

if vel > 80:
    multa = (vel - 80) * 5
    print(f"Multado em: R$ {multa:.2f}")