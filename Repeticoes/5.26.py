dividendo = int(input("Digite o dividendo: ")) 
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Erro: divisao por zero!")
else:
    resto = dividendo
    while resto >= divisor:
        resto = resto - divisor
    
    print(f"Resto da divisao: {resto}")