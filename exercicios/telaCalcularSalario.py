from flet import Page, TextField, ElevatedButton, app, Text


def main(pagina: Page):
    pagina.title = 'Calculando Salário'

    pagina.window.max_width = 600
    pagina.window.max_height = 700

    pagina.window.width = 600
    pagina.window.height = 700

    pagina.window.min_width = 400
    pagina.window.min_height = 550

    pagina.window.center()
    pagina.bgcolor = "#FFFAF0"

    t_field_nome = TextField(label="Digite o seu nome")
    t_field_salario = TextField(label="Digite seu Salário")

    btn_calcular = ElevatedButton(text="Calcular")

    def calculando(e):
        txt_resposta.value = f'10% do salário de {t_field_nome.value} é R$ {float(t_field_salario.value) * .1}'

        t_field_nome.value = ""
        t_field_nome.update()
        t_field_salario.value = ""
        t_field_salario.update()
        txt_resposta.update()

    btn_calcular.on_click = calculando

    txt_resposta = Text(value="Resposta", size=30)

    # estou usando o add para adicionar elementos na minha tela
    pagina.add(t_field_nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)

    pagina.update()


app(main)
