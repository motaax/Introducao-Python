num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
op = input("Escolha uma operacao: (+, -, *, /)")

if op == "+":
    res = num1 + num2
    print(f"Resultado: {res}")

elif op == "-":
    res = num1 - num2
    print(f"Resultado: {res}")

elif op ==  "*":
    res = num1 * num2
    print(f"Resultado: {res}")

elif op == "/":
    if num2 != 0:
        res = num1 / num2
        print(f"Resultado: {res}")
    else:
        print(f"Erro: divisao por zero!")
        
else:
    print(f"Operacao invalida!")