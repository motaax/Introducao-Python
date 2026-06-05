L = [15, 7, 27, 39]

p = int(input("Digite o valor de P: "))
v = int(input("Digite o valor de V: "))

# Procurar P
achou_p = False
x = 0
while x < len(L):
    if L[x] == p:
        achou_p = True
        pos_p = x
        break
    x += 1

# Procurar V
achou_v = False
x = 0
while x < len(L):
    if L[x] == v:
        achou_v = True
        pos_v = x
        break
    x += 1

if achou_p:
    print(f"{p} encontrado na posição {pos_p}")
else:
    print(f"{p} não encontrado")

if achou_v:
    print(f"{v} encontrado na posição {pos_v}")
else:
    print(f"{v} não encontrado")