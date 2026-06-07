def valida_string(texto, minimo, maximo):
    return minimo <= len(texto) <= maximo


print(valida_string("Python", 3, 10))   
print(valida_string("Oi", 3, 10))       
print(valida_string("Programação", 3, 10))  