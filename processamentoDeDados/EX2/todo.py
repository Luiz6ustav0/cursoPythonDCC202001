# -*- coding: utf8


import threading
import requests
import concurrent.futures as cf
import time
from functools import reduce 

class Worker(threading.Thread):
    def __init__(self, id, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self.__id = id

    def run(self):
        self.__num_lines = 0
        url = 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(self.__id, self.__id)
        content = requests.get(url)
        for i in content.text.splitlines():
            self.__num_lines += 1
                    
    def get_result(self):
        return self.__num_lines

def crawler(num_threads):
    sem = threading.BoundedSemaphore(num_threads)
    threads = []
    with open('./dados/ids.txt', 'r') as ids:
        with cf.ThreadPoolExecutor(max_workers=num_threads) as pool:
            id = ids.read().split('\n')
            arr = list(pool.map(Worker, id))
            for i in arr:
                i.start()
            for i in arr:
                i.join()
    return reduce(lambda acc, x: acc + x.get_result(), arr, 0)
