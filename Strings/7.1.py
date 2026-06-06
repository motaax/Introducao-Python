str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

posicao = str1.find(str2)

if posicao != -1:
    print(f"A segunda string ocorre na primeira. Posicao: {posicao}")
else:
    print("A segunda string nao foi encontrada.")