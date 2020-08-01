import sys

import todo

def test(case, args):
    if case == 0:
        return todo.factAll(todo.py2ll(args))
    elif case == 1:
        return todo.strAll(todo.py2ll(args))
    elif case == 2:
        return todo.incAll(todo.py2ll(args))
    elif case == 3:
        return todo.sqrAll(todo.py2ll(args))
    elif case == 4:
        return todo.isPrimeAll(todo.py2ll(args))
    elif case == 5:
        return todo.incAllN(todo.py2ll(args[1:]), args[0])
    elif case == 6:
        return todo.filterOdd(todo.py2ll(args))
    elif case == 7:
        return todo.filterPositive(todo.py2ll(args))
    elif case == 8:
        return todo.filterGtN(todo.py2ll(args[1:]), args[0])
    elif case == 9:
        return todo.filterPrimes(todo.py2ll(args))
    else:
        return None

for line in sys.stdin:
    inps = map(lambda x: int(x), list(line.split(" ")))
    case = inps[0]
    args = inps[1:]
    print(todo.ll2py(test(case, args)))