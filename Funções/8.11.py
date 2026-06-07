def encontra_string(texto, lista):
    return texto in lista


print(encontra_string("maçã", ["banana", "maçã", "uva"]))  
print(encontra_string("pera", ["banana", "maçã", "uva"]))  
print(encontra_string("Python", ["Java", "C++", "Python"]))  