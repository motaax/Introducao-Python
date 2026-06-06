texto = input("Digite uma string: ")
contagem = {}

for char in texto:
    if char in contagem:
        contagem[char] +=1 
    else:
        contagem[char] = 1

for char, qntd in contagem.items():
    print(f"'{char}' aparece {qntd} vez(es)")