import sys
from math import gcd,factorial
input=sys.stdin.readline

def dfs(L,visit,rest):
    if visit==(1<<n)-1:
        if rest==0:
            return 1
        else:
            return 0
    if dp[visit][rest]!=-1:
        return dp[visit][rest]
    for i in range(n):
        if visit&(1<<i)==0:
            dp[visit][rest]+=dfs(L+long[i],visit|(1<<i),(rest+rm[i][L])%k)
    dp[visit][rest]+=1
    return dp[visit][rest]

n=int(input())
stack=[]
for _ in range(n):
    stack.append(int(input()))
long=[]
for i in stack:
    long.append(len(str(i)))
k=int(input())
dp=[[-1]*k for _ in range(1<<n)]
rm = [[-1]*(sum(long)) for _ in range(n)]
for i in range(n):
    for j in range(sum(long)):
        rm[i][j] = (stack[i]*10**j)%k
temp=dfs(0,0,0)
F=factorial(n)
if temp==0:
    print('0/1')
else:
    v=gcd(F,dp[0][0])
    print('{}/{}'.format(temp//v,F//v))