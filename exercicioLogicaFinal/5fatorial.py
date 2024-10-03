def fatorial(numero: int) -> int:
    valorFinal = numero
    print(f'{numero}', end=' ')
    for i in range((numero - 1), 0, -1):
        print(f'x {i}', end=' ')
        valorFinal *= i
    print('=', end=' ')
    return valorFinal


print(fatorial(5))
