import flet as ft
from databases.conector import Conector
from controllers.produto_controller import ProdutoController

def produto_view(page):
    conexao = Conector.conectar()
    elementos = []

    if conexao != None:
        produtos = ProdutoController.listar(conexao)

        page.snack_bar = ft.SnackBar(ft.Text("Conexão estabelecida"))
        page.snack_bar.open = True

        desc_field = ft.TextField(label="Descrição")
        valor_field = ft.TextField(label="Valor")
        qtd_field = ft.TextField(label="Quantidade")
        salvar_button = ft.ElevatedButton(text="Salvar")

        divisor = ft.Divider(height=5)
        tabela = ft.DataTable(
        columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Produto")),
                ft.DataColumn(ft.Text("valor")),
                ft.DataColumn(ft.Text("QTD")),
            ],
            rows=[]

        )
        dt_rows = []
        for produto in produtos:
            dt_row = ft.DataRow(cells=[
                        ft.DataCell(ft.Text(produto.cod)),
                        ft.DataCell(ft.Text(produto.decricao)),
                        ft.DataCell(ft.Text(produto.preco)),
                        ft.DataCell(ft.Text(produto.qtd)),
                    ])
            dt_rows.append(dt_row)
        tabela.rows=dt_rows

        elementos.append(desc_field)
        elementos.append(valor_field)
        elementos.append(qtd_field)
        elementos.append(salvar_button)
        elementos.append(divisor)
        elementos.append(tabela)

    else:
        print("Falha na conexão!")
        page.snack_bar = ft.SnackBar(ft.Text("Falha na conexão!"))
        page.snack_bar.open = True

    return ft.Column(
        elementos
    )
