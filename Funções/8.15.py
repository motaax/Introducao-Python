import random # import random as r ; from random import randint

n = random.randint(1, 10)
tentativas = 1  

while tentativas <= 3:
    x = int(input("Escolha um numero entre 1 e 10: "))

    if x == n:
        print("Voce acertou!")
        break
    else:
        print("Voce errou!")
        tentativas += 1

if tentativas >= 3:
    print("Suas tentativas acabaram!")