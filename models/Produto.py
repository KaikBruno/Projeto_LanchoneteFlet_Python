class Produto:
                     # Metodo construtor - Instanciar o objeto
    def __init__(self, Cod, Descricao, Preco, qtd):
        self.cod=Cod # Atributo
        self.descricao=Descricao # Atributo
        self.preco=Preco # Atributo
        self.qtd=qtd # Atributo
                     # Metodos - Operações  
    def listar(self):
        print(  f" Cod: {self.cod}"+
                f" | Produto: {self.descricao[:20]:<20}"
                f" | Preço: {self.preco}"+
                f" | Qtd: {self.qtd}")

    def alterar(self, descricao, preco, qtd):
        self.descricao=descricao
        self.preco=preco
        self.qtd=qtd