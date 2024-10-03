lado1 = input('Digite a medida do primeiro lado do triângulo: ')
lado2 = input('Digite a medida do segundo lado do triângulo: ')
lado3 = input('Digite a medida do terceiro lado do triângulo: ')

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('O triângulo é equilátero')
elif (lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2):
    print('O triângulo é isóceles')
else:
    print('O triângulo é escaleno')
