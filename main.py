import flet as ft
from view.produto_view import produto_view

def main(page: ft.Page):
    page.title="Lanchonete Siri Cascudo"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window.height=600
    page.window.width=600

    page.add(produto_view(page))

ft.app(main)
        