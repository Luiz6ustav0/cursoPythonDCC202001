class Ponto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, esq_sup, dir_inf):  # Recebe dois objetos Ponto2D
        self.esq_sup = esq_sup
        self.dir_inf = dir_inf
        self.width, self.height = self.__calculate_x_and_y()

    def __calculate_x_and_y(self):
        base = self.dir_inf.x - self.esq_sup.x
        altura = self.esq_sup.y - self.dir_inf.y
        return base, altura

    def calcularArea(self):
        return abs(self.dir_inf.x - self.esq_sup.x) * abs(
            self.esq_sup.y - self.dir_inf.y
        )

    def calcularIntersecao(self, ret):
        diff_x = min(self.dir_inf.x, ret.dir_inf.x) - max(self.esq_sup.x, ret.esq_sup.x)
        diff_y = min(self.esq_sup.y, ret.esq_sup.y) - max(self.dir_inf.y, ret.dir_inf.y)
        if diff_x > 0 and diff_y > 0:
            return diff_x * diff_y
        else:
            return None
