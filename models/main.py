from databases.conector import Conector
from controllers.produto_controller import ProdutoController

conexao = Conector.conectar()

if conexao !=None:
    print("Conectado com o banco de dados")

    produtos = ProdutoController.listar(conexao, "dsadsakshd")
    if produtos!=[]:
        for produto in produtos:
            produto.listar()
        else: 
            print("Nenhum produto encontrado!")

        Conector.fechar_conecxao(conexao)

        