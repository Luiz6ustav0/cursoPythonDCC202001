class Conta:
    def __init__(self, num):
        self.conta = num
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, num, taxa):
        super().__init__(num)
        self._taxa = taxa

    def cobrar_taxa(self):
        self.saldo -= self._taxa


class ContaPoupanca(Conta):
    def __init__(self, num, juros):
        super().__init__(num)
        self._juros = juros

    def aplicar_juros(self):
        self.saldo += self.saldo * self._juros
