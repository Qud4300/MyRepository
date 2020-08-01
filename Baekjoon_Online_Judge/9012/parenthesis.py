#use List as Stack.
def isVPS(L):
    S = []
    for x in L:
        if x == '(':
            S.append(x)
        elif x == ')' and len(S):
            S.pop()
        else :
            return "NO"
    if len(S):
        return "NO"
    else:
        return "YES"

n = int(input())
for i in range(n):
    L = input()
    print(isVPS(L))
