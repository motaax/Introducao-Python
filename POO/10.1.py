class Televisao:
    def __init__(self, tamanho, marca):
        self.tamanho = tamanho
        self.marca = marca

#Criando os objetos
tv1 = Televisao(42, "Samsung")
tv2 = Televisao(55, "LG")

#Exibindo os atributos
print("TV 1:")
print("Marca:", tv1.marca)
print("Tamanho:", tv1.tamanho)

print("\nTV 2:")
print("Marca:", tv1.marca)
print("Tamanho:", tv1.tamanho)