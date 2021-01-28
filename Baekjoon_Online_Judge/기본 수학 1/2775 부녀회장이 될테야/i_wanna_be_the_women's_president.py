c = int(input())
K = []
N = []
for i in range(c):
    K.append(int(input()))
    N.append(int(input()))
for i in range(c):
    res = [x for x in range(1,N[i]+1)]
    for j in range(K[i]):
        for k in range(N[i]-1,0,-1):
            res[k] = sum(res[:k+1])
    print(res[N[i]-1])
            