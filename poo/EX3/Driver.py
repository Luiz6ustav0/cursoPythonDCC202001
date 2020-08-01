import sys
from Classes import *

"""
ATENÇÃO: VOCÊ NÃO DEVE ALTERAR ESSA PARTE DO CÓDIGO!
"""

case = int(sys.stdin.readline())

cesta = CestaCompras()

for line in sys.stdin:
    tipo, nome, valor, qtde = line.split(';')
    valor = float(valor)
    qtde = int(qtde)

    if tipo == 'L':
        item = Livro(nome, valor)
    elif tipo == 'B':
        item = Brinquedo(nome, valor)
    else:
        item = Eletronico(nome, valor)
    
    cesta.adicionar_item(item, qtde)

if case == 0:
    for item, qtde in cesta.itens.items():
        print("%s, %i" % (item.nome, qtde))
elif case == 1:
    cesta.relatorio_final()
else:
    print("Unknown case: ", case)  