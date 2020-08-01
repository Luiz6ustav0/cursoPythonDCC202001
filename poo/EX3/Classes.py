class Item:
    def __init__(self, nome, valor, desconto=0):
        self.__nome = nome
        self.__valor = valor
        self.__desconto = desconto

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @property
    def valor_com_desconto(self):
        return self.valor - self.valor * self.__desconto


class Livro(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor, desconto=0.03)


class Brinquedo(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor, desconto=0.05)


class Eletronico(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor, desconto=0.08)


class CestaCompras:
    def __init__(self):
        self._itens = {}

    @property
    def itens(self):
        return self._itens

    def adicionar_item(self, item, qtde):
        self._itens[item] = qtde

    def relatorio_final(self):
        preco_final_descontado = 0
        for item, quantity in self.itens.items():
            preco_final_descontado += item.valor_com_desconto * quantity
        print("{0:.2f}".format(preco_final_descontado))
        for key, value in self.itens.items():
            formated = "{}, {}, {}, {:.2f}, {:.2f}, {:.2f}".format(
                type(key).__name__,
                key.nome,
                value,
                key.valor,
                key.valor * value,
                key.valor_com_desconto * value,
            )
            print(formated)
