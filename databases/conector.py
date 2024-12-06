import mysql.connector

user= "root"
senha=""
host="localhost"
banco="lanchonete"

class Conector:

#retorna a conexao estabelecida ou retorna None quando der errado
    def conectar():
        conexao=None
        try:
            conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=senha,
                database=banco
            )
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com BD:{e}")

        return conexao

    #finalizar a conexao o fim das operações
    def fechar_conecxao(conexao):

        if conexao.is_connected():
            conexao.close()
            print("conexao com o bd encerrada!")

