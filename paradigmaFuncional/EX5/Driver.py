import sys
  
import todo

def test(case, args):
    if case == 0:
        return todo.delInitials(args)
    elif case == 1:
        return todo.everyOccurrence(args, 'aeiou')
    elif case == 2:
        return todo.factors(int(args[0]))
    elif case == 3:
        return todo.isPerfect(int(args[0]))
    else:
        return None

for line in sys.stdin:
    inps = line.strip().split(" ")
    case = int(inps[0])
    args = inps[1:]
    print(test(case, args))