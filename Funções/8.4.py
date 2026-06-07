def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return a

num1 = int(input("Digite um numero: ")) 
num2 = int(input("Digite outro numero: "))

print(max(num1, num2))