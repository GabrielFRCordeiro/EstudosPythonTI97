import math
import datetime as dt
import os
import time

bancoDeDados = [
    {
    "nome": "carlos",
    "senha": "1234"
    },
    {
    "nome": "tony",
    "senha": "1111"
    },
    {
    "nome": "joao",
    "senha": "@12J"
    },
]
bandeira = False

for cont in range(3):
    if bandeira == True:
        break
    os.system("cls") or None
    print("Tela de Login".center(60,"-"))
    login = input("login: ").strip().lower()
    password = input("Senha: ").strip()
    despesas = list()
    receitas = list()
    for usuario in bancoDeDados:

        if login == usuario["nome"] and password == usuario["senha"]:
            bandeira = True
            while True:
                os.system("cls") or None
                print("Tela de Menu".center(60, "-"))
                print("""
                Option
                1) Cadastrar Despesa
                2) Cadastrar Receita
                3) Mostrar Relatorio
                4) Sair
                """)
                option = input("Opção: ")
                match option:
                    case "1":
                        os.system("cls") or None
                        print("Tela Cadastrar Despesa".center(60, "-"))
                        description = input("Descrição: ")
                        value = float(input("Valor R$ "))
                        data = input("Data YYYY-MM-DD")
                        pagamento = bool(input('O pagamento foi realizado? (True ou False)'))
                        despesa = {
                            "description": description,
                            "value": value,
                            "data": data,
                            "pagamento": pagamento
                        }
                        despesas.append(despesa)
                        print("Cadastrado com sucesso !")
                    case "2":
                        os.system("cls") or None
                        print("Tela Cadastrar Receita".center(60, "-"))
                        description = input("Descrição: ")
                        value = float(input("Valor R$ "))
                        data = input("Data YYYY-MM-DD")
                        pagamento = bool(input('O pagamento foi realizado? (True ou False)'))
                        receita = {
                            "description": description,
                            "value": value,
                            "data": data,
                            "pagamento": pagamento
                        }
                        receitas.append(receita)
                        print("Cadastrado com sucesso !")
                    case "3":
                        os.system("cls") or None
                        print("Tela Relatorio".center(60, "-"))
                        totalDespesas = 0
                        totalDespesasPagas = 0
                        totalReceitas = 0
                        totalReceitasPagas = 0
                        for despesa in despesas:
                            totalDespesas += despesa["value"]
                            if despesa["pagamento"]:
                                totalDespesasPagas += despesa["value"]
                        for receita in receitas:
                            totalReceitas += receita["value"]
                            if receita["pagamento"]:
                                totalReceitasPagas += receita["value"]
                        print(f"Valor total das Receitas R$ {totalReceitas}")
                        print(f"Quantidade de Receitas {len(receitas)}")
                        print(f"Valor total das Despesas R$ {totalDespesas}")
                        print(f"Quantidade de Despesas {len(despesas)}")
                        print('-' * 50)
                        print(f'O fluxo de caixa foi {totalReceitas - totalDespesas}')
                        print(f'O fluxo de caixa já realizado foi {totalReceitasPagas - totalDespesasPagas}')
                        time.sleep(10)
                    case "4":
                        break
            break

        else:
            print("Senha o usuario incorreto !")
print("Fim do sistema")