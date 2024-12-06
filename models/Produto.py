class Produto:
                     # Metodo construtor - Instanciar o objeto
    def __init__(self, id_produto, descricao, preco, qtd):
        self.id_produto=id_produto # Atributo
        self.descricao=descricao # Atributo
        self.preco=preco # Atributo
        self.qtd=qtd # Atributo
                     # Metodos - Operações  
    def listar(self):
        print(  f" Cod: {self.id_produto}"+
                f" | Produto: {self.descricao[:20]:<20}"
                f" | Preço: {self.preco}"+
                f" | Qtd: {self.qtd}")

    def alterar(self, descricao, preco, qtd):
        self.descricao=descricao
        self.preco=preco
        self.qtd=qtd