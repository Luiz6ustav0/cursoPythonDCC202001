import sys
from Classes import *

"""
ATENÇÃO: VOCÊ NÃO DEVE ALTERAR ESSA PARTE DO CÓDIGO!
"""

case = int(sys.stdin.readline())

"""
Parametros do Retangulo1
"""
r1_se_x, r1_se_y, r1_id_x, r1_id_y = list(map(float, sys.stdin.readline().split()))
r1_esq_sup = Ponto2D(r1_se_x, r1_se_y)
r1_dir_inf = Ponto2D(r1_id_x, r1_id_y)
ret1 = Retangulo(r1_esq_sup, r1_dir_inf)

"""
Parametros do Retangulo2
"""
r2_se_x, r2_se_y, r2_id_x, r2_id_y = list(map(float, sys.stdin.readline().split()))
r2_esq_sup = Ponto2D(r2_se_x, r2_se_y)
r2_dir_inf = Ponto2D(r2_id_x, r2_id_y)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)

if case == 0:
    area1 = ret1.calcularArea()  
    print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))
elif case == 1:
    area2 = ret2.calcularArea()
    print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
elif case == 2:
    """
    Verificando intersercao
    """
    intersecao = ret1.calcularIntersecao(ret2)
    if intersecao == None:
        print(intersecao)
    else:
        print("%.2f" % intersecao)    
else:
    print("Unknown case: ", case)