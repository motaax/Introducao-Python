distancia = float(input("Digite a distancia(km): "))
velocidade = float(input("Digite a velocidade(km/h): "))

tempo = distancia / velocidade
print(f"Tempo estimado da viagem: {tempo:.2f} horas")