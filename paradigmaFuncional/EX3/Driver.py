import sys

import todo

def test(case, args):
    if case == 0:
        return todo.firstChars(args)
    elif case == 1:
        return todo.sum(map(lambda e: int(e), args))
    elif case == 2:
        return todo.avg(map(lambda e: int(e), args))
    elif case == 3:
        return todo.maxString(args)
    elif case == 4:
        return todo.buildLenFreq(args)
    elif case == 5:
        return todo.countFirsts(args)
    elif case == 6:
        return todo.mostCommonFirstChar(args)
    else:
        return None

for line in sys.stdin:
    inps = line.split(" ")
    case = int(inps[0])
    args = inps[1:]
    print(test(case, args))