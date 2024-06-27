from flet import *


def main(page: Page):
    page.title = 'Estudando Cards'
    page.window.maximized = True
    produto = Card(
        Container(
            Column([
                Row([Image('burgi.png')], alignment=MainAxisAlignment.CENTER),
                Row([Text('Burgi')], alignment=MainAxisAlignment.CENTER),
                Row([Text('Burgi Burgi')], alignment=MainAxisAlignment.CENTER),
                Row([
                    Icon(cupertino_icons.HEART, colors.RED),
                    Icon(cupertino_icons.MONEY_DOLLAR, colors.GREEN)
                ], alignment=MainAxisAlignment.SPACE_AROUND)
            ])
        ), width=300
    )

    page.add(produto)


if __name__ == '__main__':
    app(main)
