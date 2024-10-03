from datetime import date
import math


def calculaIdade(*args):
    dataNasc = date(args[2], args[1], args[0])
    idade = date.today() - dataNasc
    return f'{math.floor((idade.days + idade.seconds / 86400) / 365.2425)} anos'


print(calculaIdade(13, 11, 2000))
