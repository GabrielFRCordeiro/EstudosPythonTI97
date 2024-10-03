lista = [23, 'Carlos', True, 'Pedro', 45, 60]
soma = 0

for elemento in lista:
    if (isinstance(elemento, int) or isinstance(elemento, float)) and not (isinstance(elemento, bool)):
        soma += elemento

print(soma)
