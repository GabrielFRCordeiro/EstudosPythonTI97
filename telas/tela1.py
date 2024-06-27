import flet as ft


def main(page: ft.Page):
    page.title = 'Primeira pagina'

    # Toda vez q alterar a minha pagina, eu devo dar um update
    page.update()


if __name__ == '__main__':
    ft.app(main)
