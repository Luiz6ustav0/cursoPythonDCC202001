# -*- coding: utf8


from todo import extract_and_process
from todo import mapreduce
from todo import merge_function


import tarfile
import ssl
import sys
import urllib.request


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve('http://dcc.ufmg.br/~flaviovdf/dados.tar.gz',
                               'dados.tar.gz')
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    resultado1 = extract_and_process(tar.getmembers()[0])
    resultado2 = extract_and_process(tar.getmembers()[1])

    for line in sys.stdin:
        inps = line.strip().split(" ")
        case = int(inps[0])
        if case == 0:
            print(resultado1)
        elif case == 1:
            print(resultado2)
        elif case == 2:
            print(merge_function(resultado1, resultado2))
        else:
            final = mapreduce(1)
            print(final.most_common(3))


if __name__ == '__main__':
    main()