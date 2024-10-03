# valor1 = 12
# valor2 = 2
#
# media = (valor1 + valor2) / 2
#
# if media > 7:
#     print('Você foi aprovado')
# else:
#     print('Burro')
#
# valor1 = 11
# valor2 = 4
#
# media = (valor1 + valor2) / 2
#
# if media > 7:
#     print('Você foi aprovado')
# else:
#     print('Burro')

# Procedimento
def calcularMedia(v1: float, v2: float):
    try:
        media = (v1 + v2) / 2

        if media > 7:
            print('Você foi aprovado')
        else:
            print('Burro')
    except Exception as erro:
        print('Você digitou algo errado', erro)


calcularMedia(12, 2)
calcularMedia(11, 4)
calcularMedia(1, 'oi')


def messageDontKnow():
    print('Eu não sei de nada!')


messageDontKnow()

# Função


def calcularMedia2(v1: float, v2: float):
    try:
        media = (v1 + v2) / 2

        if media > 7:
            return 'Você foi aprovado'
        else:
            return 'Burro'
    except Exception as erro:
        return f'Você digitou algo errado {erro}'


print(calcularMedia2(1, 1))
