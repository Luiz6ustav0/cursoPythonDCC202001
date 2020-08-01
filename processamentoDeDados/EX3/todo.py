# -*- coding: utf8

from bs4 import BeautifulSoup
from functools import reduce

import multiprocessing as mp
import tarfile
from collections import Counter

def get_format_text(string):
    return (string.contents[1].text.split('- ')[1], int(string.contents[3].text.split(' ')[1]))


def extract_and_process(member):
    # observe como cada processo abre o tar novamente
    # a extração é feita por processo
    # veja exemplos do HTML na pasta exemplo
    # Para pegar o nome de um artist use texto.strip().split('-')[1].
    # O formato do texto no html é Música - Artista    
    tar = tarfile.open("dados.tar.gz", "r:gz")
    f = tar.extractfile(member)
    soup = BeautifulSoup(f, 'html.parser')
    
    dic = {}

    text_content = soup.findAll(class_="trackInfo",)
    text_content = list(map(get_format_text, text_content))
    for artist, num_plays in text_content:
        if artist in dic.keys():
            dic[artist] += num_plays  
        else:
            dic[artist] = num_plays
    return Counter(dic)

def merge_function(dict_1, dict_2):
    dict_1 = Counter(dict_1)
    dict_2 = Counter(dict_2)
    dict_1.update(dict_2.elements())
    return dict_1


def mapreduce(num_cpus=2):
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    if num_cpus > 1:
        with mp.Pool(num_cpus) as pool:
            intermed = pool.imap_unordered(extract_and_process,
                                           tar.getmembers())
    else:
        intermed = map(extract_and_process, tar.getmembers())
    final = reduce(merge_function, intermed)
    return Counter(final)

print(mapreduce().most_common(5))