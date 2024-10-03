# from typing import List
#
#
# def media(n1: float, n2: float, n3: float, n4: float) -> float:
#     '''
#     Essa função vai calcular a média de 4 notas
#     :param n1: primeira nota: float
#     :param n2: segunda nota: float
#     :param n3: terceira nota: float
#     :param n4: quarta nota: float
#     :return: float
#     '''
#     return (n1 + n2 + n3 + n4) / 4
#
#
# def media2(lista: List) -> float:
#     '''
#     Essa função vai calcular a média através de uma lista de notas: float
#     :param lista: List
#     :return: float
#     '''
#     return sum(lista) / len(lista)


# print(media(5.5, 7, 8, 10))
# print(media2([5.5, 7, 8, 10, 8, 11]))

#
# def mediaNew(*args) -> float:
#     soma = 0
#     quantNum = 0
#     for valor in args:
#         if isinstance(valor, float) or isinstance(valor, int):
#             soma += valor
#             quantNum += 1
#         elif callable(valor):
#             valor('opa')
#     return soma / quantNum
#
#
# def mensagem(texto: str) -> None:
#     print(texto)


# print(mediaNew(5.5, 7, 8, 10, 8, 11))
# print(mediaNew(5.5, 7, 8, 10, 8, 11, 'carlos', mensagem))

# lista = [23, 56, 78, 100]
# tupla = (23, 56, 78, 100)
#
# lista[0] = 'Carlos'
# print(lista)
# print(tupla)


def calculadora(*args):
    valor1 = args[1]
    valor2 = args[2]
    return args[0](valor1, valor2)


def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


print(calculadora(dividir, 1, 1))
