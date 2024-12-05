import mysql.connector
from models.Produto import Produto


user= "root"
senha=""
host="localhost"
banco="lanchonete"

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

#def inserir():C


#listar todas informacoes da tabela
def listar(conexao):
    try:
        cursor= conexao.cursor()
        query= "select * from Produto"
        cursor.execute(query)
        registros = cursor.fetchall()

        for Produto in registros:
            print(Produto)

    except mysql.connector.Error as e:
       print(f"Erro ao listar produtos:{e}")

    finally:
        cursor.close()


# atualizar uma informação da lista
def update(conexao,id_codigo_produto, preco,qtd):
    try:
        cursor = conexao.cursor()
        query = "UPDATE Produto SET preco=%s, qtd=%s WHERE id_codigo_produto=%s"
        cursor.execute(query, (preco,qtd,id_codigo_produto))
        conexao.commit()
        print(f"{id_codigo_produto} atualizado com sucesso!")
        
    except mysql.connector.Error as e:
       print(f"Erro ao atualizar o produto:{e}")

    finally:
        cursor.close()
    
#deletar uma linha a partir de seu id
def delete(conexao,id_codigo_produto,):
    try:
        cursor = conexao.cursor()
        query= " DELETE FROM Produto WHERE id_codigo_produto=%s"
        cursor.execute(query,(id_codigo_produto,))
        conexao.commit()
        print(f"{id_codigo_produto} deletado com sucesso!")


    except mysql.connector.Error as e:
       print(f"Erro ao deletar o produto:{e}")

    finally:
        cursor.close()
    

#buscar imformações de uma linha
def buscar(conexao,buscar):

    try:
        cursor = conexao.cursor()
        query = "select * from  Produto WHERE descricao like %s"
        cursor.execute(query, ("%"+buscar+"%",))
        registros = cursor.fetchall()

        for Produto in registros:
            print(Produto)
       
        
    except mysql.connector.Error as e:
       print(f"Erro ao buscar produto:{e}")

    finally:
        cursor.close()



#criar um novo registros no banco de dados
def inserir(conexao,produto):

    try:
        cursor= conexao.cursor()
        #usar o %s para evitar o sql injetor
        query = f"INSERT INTO Produto(descricao,preco,qtd) VALUES(%s,%s,%s)"
        cursor.execute(query, (produto.descricao,produto.preco,produto.qtd))
        conexao.commit()
        print(f"{produto.descricao} registrado com sucesso!")

    except mysql.connector.Error as e:
        print(f"erro ao inserir um produto:{e}")

    finally:
        cursor.close()


#main
conexao= conectar()

if conexao!=None:
    print("conectado com o banco de dados!")

    #novo_produto= Produto("x-bacon",23,2)

    #inserir(conexao,novo_produto)
    #update(conexao,4758,39,1)
    #delete (conexao,4761)
    #listar(conexao)
    buscar(conexao,"comida" )

   
    fechar_conecxao(conexao)