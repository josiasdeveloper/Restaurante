from cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def aplicar_desconto(self, desconto):
        self._preco -= (self._preco * desconto)
