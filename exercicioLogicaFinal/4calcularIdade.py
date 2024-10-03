from datetime import date
import math


def converterData(data: list) -> date:
    dataConvertida = list()
    for elemento in data:
        elementoConvertido = int(elemento)
        dataConvertida.append(elementoConvertido)
    novaData = date(dataConvertida[2], dataConvertida[1], dataConvertida[0])
    return novaData


dataNasc = input('Digite sua data de nascimento (DD/MM/AAAA): ').split('/')

dataNascConvertida = converterData(dataNasc)

idade = date.today() - dataNascConvertida
idadeEmAnos = math.floor((idade.days + idade.seconds/86400)/365.2425)

print(idadeEmAnos)
