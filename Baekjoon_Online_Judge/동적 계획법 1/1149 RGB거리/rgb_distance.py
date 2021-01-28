import sys
input = sys.stdin.readline
C = []
n = int(input())

for i in range(n):
    r,g,b = map(int, input().split())
    C.append([r,g,b])
maxCost = [C[0]]
for i in range(1,n):
    R,G,B = C[i]
    a = R + min(maxCost[i-1][1], maxCost[i-1][2])
    b = G + min(maxCost[i-1][0], maxCost[i-1][2])
    c = B + min(maxCost[i-1][0], maxCost[i-1][1])
    maxCost.append([a,b,c])
print(min(*maxCost[n-1]))
