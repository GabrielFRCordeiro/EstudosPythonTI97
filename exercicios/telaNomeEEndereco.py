from flet import Page, TextField, ElevatedButton, app, Text


def main(pagina: Page):
    pagina.title = 'Mostrando Endereço'

    pagina.window.max_width = 600
    pagina.window.max_height = 700

    pagina.window.width = 600
    pagina.window.height = 700

    pagina.window.min_width = 400
    pagina.window.min_height = 550

    pagina.window.center()
    pagina.bgcolor = "#FFFAF0"

    t_field_nome = TextField(label="Digite o seu nome")
    t_field_rua = TextField(label="Digite sua rua")
    t_field_numero = TextField(label='Digite o número da casa')
    t_field_bairro = TextField(label='Digite seu bairro')
    t_field_cep = TextField(label='Digite seu CEP')

    btn_calcular = ElevatedButton(text="Calcular")

    def calculando(e):
        txt_resposta_nome.value = f'Nome: {t_field_nome.value}'
        txt_resposta_endereco.value = f'Endereço: Rua {t_field_rua.value}, {t_field_numero.value} - Bairro: {t_field_bairro.value} - CEP: {t_field_cep.value}'

        t_field_nome.value = ""
        t_field_nome.update()
        t_field_rua.value = ""
        t_field_rua.update()
        t_field_numero.value = ""
        t_field_numero.update()
        t_field_bairro.value = ""
        t_field_bairro.update()
        t_field_cep.value = ""
        t_field_cep.update()
        txt_resposta_nome.update()
        txt_resposta_endereco.update()

    btn_calcular.on_click = calculando

    txt_resposta_nome = Text(value="Resposta Nome", size=30)
    txt_resposta_endereco = Text(value="Resposta Endereço", size=30)

    # estou usando o add para adicionar elementos na minha tela
    pagina.add(t_field_nome)
    pagina.add(t_field_rua)
    pagina.add(t_field_numero)
    pagina.add(t_field_bairro)
    pagina.add(t_field_cep)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta_nome)
    pagina.add(txt_resposta_endereco)

    pagina.update()


app(main)
