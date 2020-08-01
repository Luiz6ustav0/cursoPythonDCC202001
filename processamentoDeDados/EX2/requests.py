# -*- coding: utf8
# Esse módulo imita o requests

import urllib.request


class Get(object): pass


def get(url):
    response = urllib.request.urlopen(url)
    g = Get()
    g.status = response.status
    g.text = response.read().decode('utf-8')
    return g
