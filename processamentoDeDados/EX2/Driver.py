# -*- coding: utf8


from todo import crawler
from todo import Worker


import glob
import os
import subprocess
import sys


def main():
    for line in sys.stdin:
        inps = line.strip().split(" ")
        case = int(inps[0])
        if case <= 0:
            w = Worker(1342)
            w.run()
            print(w.get_result())
        else:
            print(crawler(case))


if __name__ == '__main__':
    main()
