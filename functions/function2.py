def verificarTamanhoString(palavra: str):
    cont = 0
    for letra in palavra:
        cont += 1

    return cont


print(verificarTamanhoString('Gege'))
