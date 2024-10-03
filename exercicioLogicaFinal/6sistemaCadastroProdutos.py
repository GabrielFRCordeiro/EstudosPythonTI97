import os
import time


def cadastrarProduto(nome: str, valor: float, data: str) -> None:
    produto = {"descricao": nome, "valor": valor, "data": data}
    estoque.append(produto)
    time.sleep(3)
    arquivo = open(file="produtos.txt", mode="a", encoding="utf-8")
    arquivo.write(f'Produto: {descricao}, Preço: R$ {valor:.2f}, Validade: {data} \n')


bancoDeDados = [{
    "nome": "tony",
    "senha": "4242"
    }, {
    "nome": "gabriel",
    "senha": "1111"
}]

estoque = list()

entrada = False
for tentativa in range(3):

    if entrada == True:
        break
    os.system("cls") or None
    print(" TELA DE LOGIN ".center(60,"="))
    login = input("Login: ").strip().lower()
    senha = input("Senha: ").strip()

    for usuario in bancoDeDados:

        if login == usuario["nome"] and senha == usuario["senha"]:
            entrada = True
            while True:
                os.system("cls") or None
                print(" SISTEMA DE CADASTRO ".center(60, "="))
                print()
                print('1) Cadastrar produto')
                print('2) Mostrar estoque')
                print('3) Sair')
                print()
                option = input("Opção: ")

                match option:
                    case "1":
                        os.system("cls") or None
                        print(" TELA DE CADASTRO ".center(60, "="))
                        descricao = input("Produto: ")
                        while True:
                            try:
                                preco = float(input("Preço: "))
                                break
                            except ValueError as erroValor:
                                print('Entrada inválida! Caso tenha digitado o valor com vírgula, digite com ponto')
                        validade = input("Validade: ")
                        print('Cadastro realizado com sucesso !')

                    case "2":
                        os.system("cls") or None
                        print(" TELA DE ESTOQUE ".center(60, "="))
                        arquivo = open(file="produtos.txt", mode="r", encoding="utf-8")
                        print(arquivo.read())
                        time.sleep(5)

                    case "3":
                        os.system("cls") or None
                        break

print(" SISTEMA ENCERRADO ".title().center(50, "="))
