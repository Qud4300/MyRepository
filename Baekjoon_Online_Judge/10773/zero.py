import sys
input = sys.stdin.readline

class Stack :
    def __init__(self) :
        self.L = list()
    def stack(self, a):
        if type(a) is int:
            self.L.append(a)
            return a
        return -1
    def pop(self):
        return self.L.pop() if len(self.L)>0 else None

n = int(input())
S = Stack()
for _ in range(n):
    a=int(input())
    if (a) == 0:
        S.pop()
    else : S.stack(a)

print(sum(S.L))
