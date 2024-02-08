from restaurantecls import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato

bebida_suco = Bebida('Suco de manga', 5.0, 'grande')
prato_sanduiche = Prato('Sanduiche', 8.0, 'Sanduiche com carne e queijo')

restaurante_parque = Restaurante('Parque', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Popular')
restaurante_japa = Restaurante('Japa', 'Sushi')

restaurante_japa.receber_avaliacao('Jonas', 10)
restaurante_japa.receber_avaliacao('Gabi', 6)
restaurante_japa.receber_avaliacao('João', 4)

restaurante_parque.adicionar_no_cardapio(prato_sanduiche)
restaurante_parque.adicionar_no_cardapio(bebida_suco)


def main():
    Restaurante.listar()
    restaurante_parque.exibir_cardapio()

if __name__ == '__main__':
    main()

