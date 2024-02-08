from avaliacao import Avaliacao
from cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome}'

    @classmethod
    def listar(cls):
        print(f'''{'Nome do restaurante'.ljust(25)} | {'Categoria do restaurante'.ljust(25)} | {'Status do restaurante'.ljust(25)} | {'Avaliação média'.ljust(25)}\n''')
        for restaurante in cls.restaurantes:
            print(f'''{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {restaurante.media_geral}''')

    @property
    def ativo(self):
        return 'O' if self._ativo else 'X'

    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_geral(self):
        if self._avaliacao:
            media = round(sum(avaliacao._nota for avaliacao in self._avaliacao)/len(self._avaliacao), 1)
            return media
        return "--"

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self.nome}')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome}| Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            if hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome}| Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)

