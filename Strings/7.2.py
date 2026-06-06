str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

comuns = ""

for caractere in str1:
    if caractere in str2 and caractere not in comuns:
        comuns += caractere

print("Caracteres comuns:", comuns)