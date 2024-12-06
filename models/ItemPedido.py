class ItemPedido:

    def __init__(self, produto, qtd, desconto, observacao) -> None:
        self.produto=produto
        self.qtd=qtd
        self.desconto=desconto
        self.observacao=observacao
        
    def imprimir(self):
         print(  f"Produto: {self.produto.descricao}\n"
                 f"|Quantidade:{self.qtd}\n"
                 f"|Desconto: {self.desconto}\n"
                 f"|Observação: {self.observacao}\n"
                 )