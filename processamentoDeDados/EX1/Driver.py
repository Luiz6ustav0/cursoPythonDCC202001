# -*- coding: utf8


from functools import reduce

from todo import conta_um_arquivo
from todo import reduz


import glob
import os
import sys

    
def main():
    pasta = os.path.join('.', 'dados', '*.txt')
    resultadomap = list(map(conta_um_arquivo, glob.glob(pasta)))
    resultadofinal = reduce(reduz, map(conta_um_arquivo, glob.glob(pasta)))
    
    for line in sys.stdin:
        inps = line.strip().split(" ")
        case = int(inps[0])
        if case == 0:
            print("{}".format(next(iter(resultadomap[0].items()))))
        elif case == 1:
            print("{}".format(next(iter(resultadomap[3].items()))))
        elif case == 2:
            print("{}".format(resultadofinal.most_common(5)))
        elif case == 3:
            print("{}".format(resultadofinal.most_common(10)))
        else:
            print(None)


if __name__ == '__main__':
    main()