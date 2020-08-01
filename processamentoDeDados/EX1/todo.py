# -*- coding: utf8


from collections import Counter


def conta_um_arquivo(fpath):
    dic = Counter()
    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:                
                palavras = line.split()
                dic.update(palavras)
    return dic


def reduz(contagens_1, contagens_2):
    contagens_1.update(contagens_2)
    return contagens_1
    