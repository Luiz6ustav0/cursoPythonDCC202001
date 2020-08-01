class Pessoa:
    def __init__ (self, idade):
        self.__idade = idade

    @property
    def idade(self):
        print('hey')
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if(idade < 10):
            print('too young...')
        print('but ok...')
        self.__idade = idade

x = Pessoa(15)
print(x.idade)
# x.idade = 5
# print(x.idade)