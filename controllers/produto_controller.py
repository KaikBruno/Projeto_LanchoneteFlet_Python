import mysql.connector

from models.Produto import Produto

class ProdutoController:

    #def inserir():C


    #listar todas informacoes da tabela
    def inserir(conexao, produto): 
        try:
            cursor= conexao.cursor()
            query= "INSERT INTO produto(descricao, preco, qtd) VALUES(%s , %s)" # Usar o "%s" para o SQL injector
            cursor.execute(query, (produto.descricao, produto.preco, produto.qtd))
            conexao.commit()
            print(f'{produto.descricao}, registrado com sucesso!')

        except mysql.connector.Error as e:
            print(f"Erro ao listar produtos:{e}")

        finally:
            cursor.close()

    # R - Read retorna uma lista de objeto peoduto
    def listar(conexao):
        listaProdutos=[]
        try:
            cursor = conexao.cursor()
            query = "Select * from produto"
            cursor.execute(query)
            registros = cursor.fetchall()
        
            for registro in registros:
                objeto = Produto(*registro)   #Produto (registro[0], registro[1],registro[2]....)
                listaProdutos.append(objeto)
        
        except mysql.connector.Error as e:
            print(f"Erro ao listar produtos:{e}")  
        finally:
            cursor.close()
        return listaProdutos


    # atualizar uma informação da lista
    def update(conexao,id_produto, preco,qtd):
        try:
            cursor = conexao.cursor()
            query = "UPDATE Produto SET preco=%s, qtd=%s WHERE id_codigo_produto=%s"
            cursor.execute(query, (preco,qtd,id_produto))
            conexao.commit()
            print(f"{id_produto} atualizado com sucesso!")
            
        except mysql.connector.Error as e:
         print(f"Erro ao atualizar o produto:{e}")

        finally:
         cursor.close()
        
    #deletar uma linha a partir de seu id
    def delete(conexao,id_produto,):
        try:
            cursor = conexao.cursor()
            query= " DELETE FROM Produto WHERE id_produto=%s"
            cursor.execute(query,(id_produto,))
            conexao.commit()
            print(f"{id_produto} deletado com sucesso!")


        except mysql.connector.Error as e:
            print(f"Erro ao deletar o produto:{e}")

        finally:
            cursor.close()
        

    #buscar imformações de uma linha
    def buscar(conexao,buscar):

        listaProduto = []
        try:
            cursor = conexao.cursor()
            query = "select * from  Produto WHERE descricao like %s"
            cursor.execute(query, ("%"+buscar+"%",))
            registros = cursor.fetchall()

            for Produto in registros:
                objeto = Produto(*Produto)
            listaProduto.append()
        
            
        except mysql.connector.Error as e:
         print(f"Erro ao buscar produto:{e}")

        finally:
         cursor.close()
        return listaProduto




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


    