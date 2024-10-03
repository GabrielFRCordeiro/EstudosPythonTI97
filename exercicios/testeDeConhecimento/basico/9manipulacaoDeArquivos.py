def escreveAlgo(algo: str) -> None:
    arquivo = open('texto.txt', 'a', encoding='utf-8')
    arquivo.write(f'{algo}\n')
    arquivo.close()

def leArquivo() -> list:
    arquivo = open('texto.txt', 'r', encoding='utf-8')
    linhas = list()
    for linha in arquivo.readlines():
        linhas.append(linha.replace('\n', ''))
        arquivo.close()
    return linhas

escreveAlgo('oi')
escreveAlgo('tchau')
escreveAlgo('sei la')
print(leArquivo())
