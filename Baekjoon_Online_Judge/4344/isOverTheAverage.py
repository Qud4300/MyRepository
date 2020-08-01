c = int(input())
N = [0]*c
Avg = [0]*c
for i in range(c):
    N[i] = list(map(int, input().split()))
    Avg[i] = sum(N[i][1:])/N[i][0]
    pct = len(list(x for x in N[i][1:] if x>Avg[i]))/N[i][0]*100
    print("%.3f" %(pct),'%', sep='')
