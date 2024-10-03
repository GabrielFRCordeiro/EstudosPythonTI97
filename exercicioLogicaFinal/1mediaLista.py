valores = list()

for i in range(4):
    numero = float(input('Digite um numero: '))
    valores.append(numero)

media = sum(valores) / len(valores)

print(f'A média dos valores é {media}')
