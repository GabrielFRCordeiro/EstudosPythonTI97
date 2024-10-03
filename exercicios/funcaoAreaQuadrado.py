def areaQuadrado(lado: float) -> float:
    area = lado ** 2
    return area


ladoQuadrado = float(input('Digite a medida do lado do quadrado: '))
print(f'A área do quadrado de lado {ladoQuadrado} é {areaQuadrado(ladoQuadrado)}')
