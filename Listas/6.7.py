expressao = input("Digite a expressao: ")

pilha = []
erro = False

for char in expressao:
    if char == "(":
        pilha.append(char)
    elif char == ")":
        if len(pilha) == 0:
            erro = True
            break
        pilha.pop()

if erro or len(pilha) != 0:
    print("Erro")
else :
    print("OK")