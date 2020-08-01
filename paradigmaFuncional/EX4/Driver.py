import sys
import todo
  
def show(L):
    for line in L:
        print (line)

case = int(sys.stdin.readline())
lines = map(lambda x: x.strip().replace(" ", "").split(","), sys.stdin)

if case == 0:
    show(todo.lastNames(lines))
elif case == 1:
    show(todo.citations(lines))
elif case == 2:
    show(todo.fullCitations(lines))
else:
    print("Unknown case: ", case)